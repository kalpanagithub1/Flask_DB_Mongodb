from flask import Flask
from flask import request
from flask import render_template
from pymongo import MongoClient 
from flask_pymongo import PyMongo

app = Flask("MyApp")


app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/database"
mongo = PyMongo(app)
student_collection = mongo.db.students
@app.route('/form')
def form():
    return render_template("form.html")



@app.route('/result', methods=['POST'])
def result():
    name = request.form.get("a1")
    contact = request.form.get("a2")
    email = request.form.get("a3")
    college= request.form.get("a4")


    if name != "" and contact != "" and email != "" and college != "":
            student = student_collection.insert_one({"Name": name, "Contact": contact, "E-mail": email, "College":college})
            return render_template("submit_page.html")

@app.route("/read")
def read_data():
    student = (student_collection.find())
    if student != "":
        return render_template('index.html', student=student)
    else:
        return "There is nothing to show"

@app.route("/delete")
def delete():
    student_collection.remove({})
    return render_template("delete_page.html")

app.run(port=1234, debug=True)