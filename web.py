from flask import Flask,render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "<span style='font-weight: 700'><span style='font-size: 30px'>資管二A 411146253 陳彥傑的求職相關資訊</span><br>"
    X += "<span style='font-size: 25px'><a href=/about style='text-decoration:none'>我的個人簡介</a><br>"
    X += "<span style='font-size: 25px'><a href=/work style='text-decoration:none'>MIS相關工作介紹<a><br>"
    X += "<span style='font-size: 25px'><a href=/ucan style='text-decoration:none'>職涯測驗結果<a><br>"
    X += "<span style='font-size: 25px'><a href=/autobiography style='text-decoration:none'>求職履歷自傳<a><br>"
    return X

@app.route("/about")
def course():
    return render_template("about.html")

@app.route("/work")
def today():
    return render_template("work.html")

@app.route("/ucan")
def about():
   return render_template("ucan.html")

@app.route("/autobiography")
def welcome():
    return render_template("autobiography.html") 


if __name__ == "__main__":
    app.run()
