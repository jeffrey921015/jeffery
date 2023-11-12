from flask import Flask,render_template
from datetime import datetime
from waitress import serve


app = Flask(__name__)

@app.route("/")
def index():
    X = "資管二A 411146253 陳彥傑<br>"
    X += "<a href=/mis>資管導論<br>"
    X += "<a href=/today>今日日期<a><br>"
    X += "<a href=/about>彥傑個人網頁<a><br>"
    return X

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    #app.run()
    serve(app, host='0.0.0.0', port=8080)

