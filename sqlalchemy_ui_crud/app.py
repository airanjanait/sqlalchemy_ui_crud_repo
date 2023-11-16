from flask import Flask,render_template,request,redirect
from fun import crud
from database import get_db


get_db()
app=Flask(__name__)
obj=crud()


#______________insert route______________

@app.route("/",methods=["GET","POST"])
def insert():
    if request.method=="POST":
        data=""
        emp_name=request.form.get("emp_name")
        DOJ=request.form.get("DOJ")
        MOnumber=request.form.get("MOnumber")
        data=emp_name,DOJ,MOnumber
        obj.insert(data)
    return render_template("form.html")

#_______________fetching all data ______________________

@app.route("/fetch_data")
def fetch():
    data=""
    data=obj.fetch_data()
    print(data,"------------------------------")
    return render_template("table.html",data=data)

#_______________delete data _____________________________

@app.route("/delete/<emp_name>")
def delete(emp_name):
    obj.delete_data(emp_name)
    return redirect("/fetch_data")

#_____________fetch one data to update_____________________

@app.route("/fetchtoupdate/<id>")
def fetchtoupdate(id):
    data=obj.fetchonedata(id)
    return render_template("update_form.html",data=data)

#________________update route______________________

@app.route("/update",methods=["POST","GET"])
def update():
    if request.method=='POST':
        id=request.form.get("id")
        emp_name=request.form.get("emp_name")
        DOJ=request.form.get("DOJ")
        MOnumber=request.form.get("MOnumber")
        obj.update(emp_name,DOJ,MOnumber,id)
    return redirect ("/fetch_data")



if __name__=="__main__":
    app.run(debug=True)