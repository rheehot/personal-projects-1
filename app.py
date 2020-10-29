from bs4.element import ResultSet, SoupStrainer
from flask import Flask, request, render_template, redirect
from flask.helpers import url_for
from bs4 import BeautifulSoup
import datetime
import pymysql


app = Flask(__name__)

db = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="board_test",
    charset="utf8"
)
cur = db.cursor()


@app.route("/")
def home():
    sql = "SELECT * FROM board"
    cur.execute(sql)
    data_list = cur.fetchall()
    return render_template("index.html", data_list=data_list)


@app.route("/write", methods=['GET', 'POST'])
def write():
    if request.method == 'POST':

        # post method 를 통해 write 페이지 접속 후, form 데이터를 받아야 함
        board_title = request.form['board_title']
        board_text = request.form['board_text']
        board_writer = request.form['board_writer']
        board_submit = datetime.datetime.now().strftime("%Y-%m-%d")

        # 데이터베이스 목록 가져오기
        sql = "INSERT INTO board (board_title, board_text, board_writer, board_submit) VALUES (%s, %s, %s, %s);"
        cur.execute(sql, (board_title, board_text, board_writer, board_submit))
        db.commit()

        # 마지막으로 insert 한 데이터메이서 primary key 가져오기
        sql = "SELECT last_insert_id()"
        last_row_id = cur.lastrowid
        find_one = "SELECT * FROM board WHERE id = %d" % last_row_id

        # title
        cur.execute(find_one)
        title = cur.fetchone()[1]

        # contents
        cur.execute(find_one)
        contents = cur.fetchone()[2]

        # writer
        cur.execute(find_one)
        writer = cur.fetchone()[3]

        # date
        cur.execute(find_one)
        sub_date = cur.fetchone()[4]

        return render_template("view.html", sub_date=sub_date, title=title, contents=contents, writer=writer)

    else:
        return render_template("write.html")


if __name__ == "__main__":
    app.run()
