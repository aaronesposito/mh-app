from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/create", methods=['GET', 'POST'])
def create_entry():
    if request.method == 'POST':
        data = [int(request.form['focus']),
                int(request.form['mood']),
                float(request.form['sleep']),
                request.form['notes']]

        con = sqlite3.connect("mentalhealth.db")
        cur = con.cursor()
        cur.execute("INSERT INTO day(focus, mood, sleep, note) VALUES(?, ?, ?, ?)", data)
        con.commit()
        con.close()
        return render_template('home.html')
    else:
        return render_template('form.html')

@app.route("/view")
def view_entries():
    data_tuples = []
    con = sqlite3.connect("mentalhealth.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM day ORDER BY date"):
        data_tuples.append(row)
    con.close()

    data = {
        "dates": [row[0][:-3] for row in data_tuples],
        "moods": [row[1] for row in data_tuples],
        "sleeps": [row[2] for row in data_tuples],
        "focuses": [row[4] for row in data_tuples],
        "notes": [row[3] for row in data_tuples]
    }

    for key, values in data.items():
        values.reverse()


    return render_template('view.html', data=data)
