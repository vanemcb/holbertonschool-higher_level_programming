#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """

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
    sql = "SELECT * FROM states ORDER BY id"


    # Execute SQL query
    cursor.execute(sql)

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print elements
    for element in results:
        print(element)

    cursor.closed()

    # Disconnect from server
    db.close()
