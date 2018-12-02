import sqlite3
from constants import *
from flask import request

# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = sqlite3.connect('mysite/example.db')
    return render_template("index.html",yachts=getYachts(conn),directions=getDirections(conn),yacht_types=getYachtTypes(conn))

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        return render_template("search.html")
    else:
        return render_template("admin.html")


@app.route('/search')
def search():
    conn = sqlite3.connect('mysite/example.db')
    date_start = request.args.get('date_start')
    if date_start is None:
        date_start = 0
    date_finish = request.args.get('date_finish')
    if date_finish is None:
        date_finish = 0
    yacht_type = request.args.get('yacht_type')
    if yacht_type is None:
        yacht_type = 0
    yacht_seat = request.args.get('yacht_seat')
    if yacht_seat is None:
        yacht_seat = 0
    price_finish = request.args.get('price_finish')
    if price_finish is None:
        price_finish = 99999999
    price_start = request.args.get('price_start')
    if price_start is None:
        price_start = 0


    y = getYachtsFilter(conn,date_start,date_finish,yacht_type,yacht_seat,price_start,price_finish)
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

def getYachtsFilter(conn,date_start=0,date_finish=0,yacht_type=0,seat=0,price_start=0,price_finish=15000):
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yachts WHERE yacht_price BETWEEN ? AND ? AND yacht_seat >= ?", (price_start,price_finish,seat))
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