from flask import Flask, render_template, request
from crud import add, get
from apicall import random_xkcd

app = Flask(__name__)

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
        return render_template('home.html')
    else:
        return render_template('form.html')

@app.route("/view", methods=["GET", "DELETE"])
def view_entries(): 
    if request.method == 'GET':   
        data_tuples = get()
        data = {
            "dates": [row[0][5:11] for row in data_tuples],
            "moods": [row[1] for row in data_tuples],
            "sleeps": [row[2] for row in data_tuples],
            "focuses": [row[4] for row in data_tuples],
            "notes": [row[3] for row in data_tuples]
        }
        return render_template('view.html', data=data)
    if request.method == "DELETE":
        pass