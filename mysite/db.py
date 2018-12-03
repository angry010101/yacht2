import sqlite3
from constants import *
import random

def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    yacht_types = c.execute("""CREATE TABLE 'table_yacht_types'
             ('id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'yacht_type_desc' TEXT)
             """)

    yachts = c.execute("""CREATE TABLE 'table_yachts'
             ('yacht_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'yacht_name' TEXT,'yacht_price' REAL,
             'yacht_rate' REAL, 'yacht_seat' INTEGER,
             'yacht_type' INT,
             'yacht_description' TEXT,'yacht_pdf' TEXT,
             FOREIGN KEY ('yacht_type') REFERENCES 'table_yacht_types' ('id'))
             """)

    directions = c.execute("""CREATE TABLE 'table_directions'
            ('direction_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'direction_title' TEXT,'direction_price' REAL)
             """)

    photos = c.execute("""CREATE TABLE 'table_photos'
             ('photo_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'photo_yachtid' INTEGER,'photo_link' TEXT,
             FOREIGN KEY ('photo_yachtid') REFERENCES 'table_yachts' ('yacht_id'))""")

    order = c.execute("""CREATE TABLE 'table_orders'
            ('order_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'order_yacht' INTEGER,'order_startdate' INTEGER,
             'order_finishdate' INTEGER, 'order_peoplecount' INTEGER,
             FOREIGN KEY ('order_yacht') REFERENCES 'table_yachts' ('yacht_id'))
             """)

    services = c.execute("""CREATE TABLE 'table_services'
            ('service_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'service_price' REAL,'service_title' TEXT,
             'service_isstuff' INTEGER)
             """)

    built_in = c.execute("""CREATE TABLE 'table_built'
            ('built_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'built_title' TEXT)""")

    order_service = c.execute("""CREATE TABLE 'table_order_service'
            ('order_service_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'order_service_serviceid' INT,
             'order_service_orderid' INT,
             FOREIGN KEY ('order_service_serviceid') REFERENCES 'table_service' ('service_id'),
             FOREIGN KEY ('order_service_orderid') REFERENCES 'table_order' ('order_id'))""")


    yacht_built = c.execute("""CREATE TABLE 'table_yacht_built'
            ('yacht_built_id' INTEGER PRIMARY KEY AUTOINCREMENT,
             'yacht_built_builtid' INT,
             'yacht_built_yachtid' INT,
             FOREIGN KEY ('yacht_built_yachtid') REFERENCES 'table_yachts' ('yacht_id'),
             FOREIGN KEY ('yacht_built_builtid') REFERENCES 'table_built' ('built_id')
             )""")

    conn.commit()
    conn.close()

    return 'OK'

def drop_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    try:
        r = c.execute("""DROP TABLE 'table_yacht_types'""")
    except:
        print("yacht_Types isnot dropped")
        pass
    try:
        r = c.execute("""DROP TABLE 'table_directions'""")
    except:
        pass
    try:
        r = c.execute("""DROP TABLE 'table_yachts'""")
    except:
        pass
    try:
        r = c.execute("""DROP TABLE 'table_orders'""")
    except:
        pass
    try:
        r = c.execute("""DROP TABLE 'table_services'""")
    except:
        pass
    try:
        r = c.execute("""DROP TABLE 'table_photos'""")
    except:
        pass
    try:
        r = c.execute("""DROP TABLE 'table_built'""")
    except:
        pass
    try:
        r = c.execute("""DROP TABLE 'table_order_service'""")
    except:
        pass
    try:
        r = c.execute("""DROP TABLE 'table_yacht_built'""")
    except:
        pass


    conn.commit()
    conn.close()
    return "OK"

def add_data(i=0):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    item = [None,"Doom" + str(i),int(random.uniform(10000.5, 19000)),random.uniform(0,5),random.randint(10, 50),random.randint(0, 1),"Lorem ipsum dolor sit amend this yacht the best","https://google.com"]
    c.execute('insert into table_yachts values (?,?,?,?,?,?,?,?)', item)
    conn.commit()
    conn.close()
    return "OK"

def add_cities():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    item = [None,"Kiyov" + str(random.randint(1, 50)),int(random.uniform(10000.5, 19000))]
    c.execute('insert into table_directions values (?,?,?)', item)
    conn.commit()
    conn.close()
    return "OK"


def add_yacht_types():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    item = [None,"Парусная"]
    c.execute('insert into table_yacht_types values (?,?)', item)

    item = [None,"Моторная"]
    c.execute('insert into table_yacht_types values (?,?)', item)
    conn.commit()
    conn.close()
    return "OK"
def init():
    print(init_db())
    print(add_yacht_types())
    for i in range(0,10):
        #print(add_data())
        print(add_cities())
init()
print("OK")
for i in range(0,100):
    print(add_data(i))

#drop_db()