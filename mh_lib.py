import requests
from random import randint
import sqlite3


def random_xkcd():
    comic_number = randint(0, 3057)
    response = requests.get(f"https://xkcd.com/{comic_number}/info.0.json")
    data = response.json()
    return data

def add(data):
    con = sqlite3.connect("mentalhealth.db")
    cur = con.cursor()
    cur.execute("INSERT INTO day(focus, mood, sleep, note) VALUES(?, ?, ?, ?)", data)
    con.commit()
    con.close()

def get():
    data_tuples = []
    con = sqlite3.connect("mentalhealth.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM day ORDER BY date"):
        data_tuples.append(row)
    con.close()
    return data_tuples

def add_journal(data):
    con = sqlite3.connect("mentalhealth.db")
    cur = con.cursor()
    cur.execute("INSERT INTO journals(entry, title) VALUES(?, ?)", data)
    con.commit()
    con.close()

def get_journals():
    data_tuples = []
    con = sqlite3.connect("mentalhealth.db")
    cur = con.cursor()
    for row in cur.execute("SELECT * FROM journals ORDER BY created_on"):
        data_tuples.append(row)
    con.close()
    return data_tuples
