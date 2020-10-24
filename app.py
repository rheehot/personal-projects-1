from flask import Flask, request, render_template
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

sql = "SELECT * from board"
cur.execute(sql)

data_list = cur.fetchall()


@app.route("/")
def home():
    return render_template("index.html", data_list=data_list)


if __name__ == "__main__":
    app.run()
