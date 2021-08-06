#!/usr/bin/python3
""" Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument """

from sys import argv
import MySQLdb

if __name__ == "__main__":

    # Open database connection
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    # Cursor object
    cursor = db.cursor()

    # SQL query
    sql = "SELECT * FROM states WHERE name LIKE '{}%' ORDER BY id".format(argv[4])

    # execute SQL query
    cursor.execute(sql)

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print elements
    for element in results:
        print(element)

    cursor.close()

    # Disconnect from server
    db.close()
