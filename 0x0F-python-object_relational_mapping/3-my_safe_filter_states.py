#!/usr/bin/python3
""" cript that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time, write one that
is safe from MySQL injections """

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
    n = (argv[4],)
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id", n

    # execute SQL query
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id", (argv[4],))

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print elements
    for element in results:
        print(element)

    cursor.close()

    # Disconnect from server
    db.close()
