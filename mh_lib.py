import requests
from random import randint
import psycopg2
from dotenv import load_dotenv
import os
from db_init import initialize_conn


def random_xkcd():
    comic_number = randint(0, 3057)
    response = requests.get(f"https://xkcd.com/{comic_number}/info.0.json")
    data = response.json()
    return data

def add(data):
    conn = initialize_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO day(focus, mood, sleep, note) VALUES(%s, %s, %s, %s)", data)
    conn.commit()
    cur.close()
    conn.close()

def get():
    conn = initialize_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM day ORDER BY date")
    data_tuples = cur.fetchall()
    cur.close()
    conn.close()
    return data_tuples

def add_journal(data):
    conn = initialize_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO journals(entry, title) VALUES(%s, %s)", data)
    conn.commit()
    cur.close()
    conn.close()

def get_journals():
    conn = initialize_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM journals ORDER BY created_on")
    data_tuples = cur.fetchall()
    cur.close()
    conn.close()
    return data_tuples
