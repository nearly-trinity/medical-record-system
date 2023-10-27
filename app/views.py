from app import app
from flask import render_template
from app.forms import PatientSearchForm


@app.route("/")
def helloworld():
    return "main page"


@app.route("/search", methods=["GET", "POST"])
def search():
    form = PatientSearchForm()

    # this eventually will be a db query
    search_results = {"First Name": "Billy", "Last Name": "Bob", "ID Number": 1}

    if form.validate_on_submit():
        print("validating form submission")

    return render_template("search.html", form=form, results=search_results)


@app.route("/newPatient")
def addNewPatient():
    print("add new patient")
    return "newpatient"


@app.route("/druglist")
def druglist():
    return "druglist"


@app.route("/healthhistory")
def healthhistory():
    return "healthhistory"


@app.route("/socialhistory")
def socialhistory():
    return "socialhistory"


@app.route("/visitforms")
def visitforms():
    return "visitforms"
