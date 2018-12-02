import sqlite3
from constants import *
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('mysite/example.db')
    return render_template("index.html",yachts=getYachts(conn),directions=getDirections(conn),yacht_types=getYachtTypes(conn))

@app.route('/search')
def search():
    conn = sqlite3.connect('mysite/example.db')
    y = getYachtsFilter(conn)
    return render_template("search.html",yachts=y,directions=getDirections(conn),yacht_types=getYachtTypes(conn),results_count=len(y))

@app.route('/yacht')
def yacht():
    return render_template("yacht.html")

@app.route('/i')
def id():
    conn = sqlite3.connect('mysite/example.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yachts")
    rows = cur.fetchall()

    return str(rows)

def getYachts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yachts")
    rows = cur.fetchall()
    return rows

def getYachtsFilter(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yachts")
    rows = cur.fetchall()
    return rows


def getDirections(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_directions")
    rows = cur.fetchall()
    return rows


def getYachtTypes(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yacht_types")
    rows = cur.fetchall()
    return rows