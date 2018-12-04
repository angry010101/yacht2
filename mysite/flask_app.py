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
    conn = sqlite3.connect('mysite/example.db')
    if request.method == 'POST':
        conn = sqlite3.connect('mysite/example.db')
        date_start = request.args.get('date_start')
        if date_start is None:
            date_start = 0
        date_finish = request.args.get('date_finish')
        if date_finish is None:
            date_finish = 0
        yacht_type = request.args.get('yacht_type[]')
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

        direction = request.args.get('directions[]')
        if direction is None:
            direction = 0

        offset = request.args.get('offset')
        if offset is None:
            offset = 0

        order = request.args.get('order')
        if order is None:
            order = "rank"
        import math

        y,max_price,results_count = getYachtsFilter(conn,offset,date_start,date_finish,yacht_type,yacht_seat,price_start,price_finish,order)
        if max_price is None:
            max_price = 99999

        pagination_count =math.ceil(results_count/10)
        params = [date_finish,date_start,yacht_seat,yacht_type,price_start,price_finish,direction,pagination_count,int(math.ceil(int(offset)/10)),order]
        y,max_price,results_count = getYachtsFilter(conn,offset,date_start,date_finish,yacht_type,yacht_seat,price_start,price_finish)

        return render_template("search_admin.html",yachts=y,directions=getDirections(conn),yacht_types=getYachtTypes(conn),results_count=results_count,max_price=max_price,params=params)
    else:
        return render_template("admin.html")


@app.route('/secret')
def secret():
    f=open("secret.txt", "r")
    if f.mode == 'r':
        contents =f.read()
    return contents

@app.route('/write',methods=['POST'])
def write():
    if request.method == 'POST':
        number = request.form['number']
        if number is None:
            return "number is none"
        f=open("secret.txt", "w+")
        f.write(number)
        return "OK"
    else:
        return "INVALID METHOD"

@app.route('/clear',methods=['GET','POST'])
def clear1():
    f=open("secret.txt", "w+")
    f.write("")
    return "OK"

@app.route('/search')
def search():
    conn = sqlite3.connect('mysite/example.db')
    date_start = request.args.get('date_start')
    if date_start is None:
        date_start = 0
    date_finish = request.args.get('date_finish')
    if date_finish is None:
        date_finish = 0
    yacht_type = request.args.get('yacht_type[]')
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

    direction = request.args.get('directions[]')
    if direction is None:
        direction = 0

    offset = request.args.get('offset')
    if offset is None:
        offset = 0

    order = request.args.get('order')
    if order is None:
        order = "rank"
    import math

    y,max_price,results_count = getYachtsFilter(conn,offset,date_start,date_finish,yacht_type,yacht_seat,price_start,price_finish,order)
    if max_price is None:
        max_price = 99999

    pagination_count =math.ceil(results_count/10)
    params = [date_finish,date_start,yacht_seat,yacht_type,price_start,price_finish,direction,pagination_count,int(math.ceil(int(offset)/10)),order]
    return render_template("search.html",yachts=y,directions=getDirections(conn),yacht_types=getYachtTypes(conn),results_count=results_count,max_price=max_price,params=params)

@app.route('/yacht')
def yacht():
    conn = sqlite3.connect('mysite/example.db')
    id = request.args.get('id')
    if id is None:
        id = 0
    y = getYacht(conn,id)
    return render_template("yacht.html",yacht=y,directions = getDirections(conn))

@app.route('/i')
def id():
    conn = sqlite3.connect('mysite/example.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yachts")
    rows = cur.fetchall()

    return str(rows)


def getYacht(conn,id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yachts WHERE yacht_id=?",(str(id),))
    row = cur.fetchone()
    return row

def getYachts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM table_yachts")
    rows = cur.fetchall()
    return rows

def getYachtsFilter(conn,offset=0,date_start=0,date_finish=0,yacht_type=0,seat=0,price_start=0,price_finish=99999,order="rank"):
    cur = conn.cursor()


    if (order=="rank"):
        order = "yacht_rate"
    else:
        order = "yacht_price"
    cur.execute("SELECT count(*) FROM table_yachts WHERE yacht_price BETWEEN ? AND ? AND yacht_seat >= ?", (price_start,price_finish,seat))
    results_count = cur.fetchall()
    results_count = results_count[0][0]
    cur.execute("SELECT * FROM table_yachts WHERE yacht_price BETWEEN ? AND ? AND yacht_seat >= ? ORDER BY " + order + " LIMIT 10 OFFSET ? ", (price_start,price_finish,seat,offset))
    rows = cur.fetchall()
    cur.execute("SELECT max(yacht_price) FROM table_yachts")
    max_price = cur.fetchall()
    return rows,max_price,results_count


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