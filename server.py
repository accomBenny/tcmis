from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
	homepage = "<h1>顏秉庭Python網頁</h1>"
	homepage += "<a href=/mis>MIS</a><br>"
	homepage += "<a href=/today>顯示日期時間</a><br>"
	homepage += "<a href=/welcome?nick=顏秉庭>傳送使用者暱稱</a><br>"
	homepage += "<a href=/about>秉庭簡介網頁</a><br>"
	homepage += "<a href=/account>網頁輸入帳密</a><br>"
	return homepage

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

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
	user = request.values.get("nick")
	return render_template("welcome.html", name=user)

if __name__ == "__main__":
	app.run()
	serve(app, host='0.0.0.0', port=8080)