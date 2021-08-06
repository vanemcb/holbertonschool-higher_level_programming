#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument """

from sys import argv
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=argv[1],
    passwd=argv[2],
    db=argv[3]
)

cursor = db.cursor()

sql = "SELECT * FROM states WHERE name LIKE '{}%' ORDER BY id".format(argv[4])

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for element in results:
        print(element)
except:
    print("Error!!")

cursor.close()
db.close()
