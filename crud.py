import sqlite3


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