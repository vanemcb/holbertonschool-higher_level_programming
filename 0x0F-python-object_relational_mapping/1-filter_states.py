#!/usr/bin/python3
""" Script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    port=3307,
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)

cursor = db.cursor()

sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for element in results:
        print(element)
except:
    print("Error!!")

db.close()
