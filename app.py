from flask import Flask
from flask import render_template,request,redirect
app = Flask(__name__)

@app.route("/") #This is the front page
def info():
	return render_template("main.html")
	return redirect("/welcome")

@app.route("/welcome", methods = ["POST"]) #This is where we take the input
def wel():
	return render_template("index.html")

@app.route("/submit" , methods = ["POST"])
def submit_endpoint():
	return redirect("/view")


print("Starting Application")
app.run(debug=True)
