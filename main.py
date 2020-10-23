from flask import Flask, render_template, request
import datetime, timedelta

app = Flask("Hello World!")

TODAY = datetime.datetime.today()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/d-day")
def dday():
    d_day = request.args.get("d_day_cal")
    today = TODAY
    convertToDay = datetime.datetime.strptime(d_day, "%Y-%m-%d")
    days = today - convertToDay
    days = days.days

    return render_template(
        "day.html", calculateBy=d_day, dateType=convertToDay, today=today, result=days)


app.run(host="0.0.0.0")
