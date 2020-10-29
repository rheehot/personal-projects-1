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


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        sql = "SELECT * from board"
        cur.execute(sql)
        data_list = cur.fetchall()
        return render_template("index.html", data_list=data_list)
    elif request.method == 'POST':
        board_title = request.form['board_title']
        board_text = request.form['board_text']
        board_writer = request.form['board_writer']
        board_submit = datetime.datetime.now().strftime("%Y-%m-%d")
        sql = "INSERT INTO board (board_title, board_text, board_writer, board_submit) VALUES (%s, %s, %s, %s);"
        cur.execute(sql, (board_title, board_text, board_writer, board_submit))
        db.commit()
    return redirect(url_for('home'))


@app.route("/write", methods=['GET', 'POST'])
def write():
    return render_template("write.html")


# @app.route("/view", methods=['GET', 'POST'])
# def view():
#     return render_template("view.html")


@app.route("/login", methods=['GET', 'POST'])
def view():
    return render_template("login.html")


if __name__ == "__main__":
    app.run()
