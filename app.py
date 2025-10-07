from flask import Flask, render_template, request, redirect, url_for
from mh_lib import add, get, random_xkcd, add_journal, get_journals, check_credential
from flask_cors import CORS
import os
from db_init import initialize_database
import json
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)
load_dotenv()
initialize_database()


@app.route("/")
def home():
    comic = random_xkcd()
    return render_template('home.html', img=comic["img"], title=comic["title"])

@app.route("/create", methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        data = [int(request.form['focus']),
                int(request.form['mood']),
                float(request.form['sleep']),
                request.form['notes']]
        add(data)        
        return redirect("/")
    else:
        return render_template('form.html')

@app.route("/view", methods=["GET", "DELETE"])
def view_entries(): 
    if request.method == 'GET':   
        data_tuples = get()
        data = {
            "dates": [row[0].strftime("%Y-%m-%d") for row in data_tuples],
            "moods": [row[1] for row in data_tuples],
            "sleeps": [row[2] for row in data_tuples],
            "focuses": [row[4] for row in data_tuples],
            "notes": [row[3] for row in data_tuples]
        }
        return render_template('view.html', data=data)
    if request.method == "DELETE":
        pass


@app.route("/create_journal", methods=["GET", "POST"])
def create_journal():
    if request.method == "POST":
        try:
            data = [request.form['entry'], request.form['title']]
            add_journal(data)
        except:
            print(request.form)
        return redirect("/")
    else:
        return render_template('journal_entry.html')
    
@app.route("/view_journals", methods=["GET", "DELETE"])
def view_journals():
    data_tuples = get_journals()
    data = []
    i = 0
    for row in data_tuples[::-1]:
        data.append([i, row[0].strftime("%Y-%m-%d"), row[1], row[2]])
        i+=1
    data.reverse()
    return render_template('journal_view.html', data=data)

    
if __name__ == "__main__":
    #PROD
    from waitress import serve
    serve(app, host="0.0.0.0", port=5001)

    #DEV
    # app.run(debug=True)
    