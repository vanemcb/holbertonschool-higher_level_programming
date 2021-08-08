#!/usr/bin/python3
""" Script that lists all cities from the database hbtn_0e_4_usa """

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
    sql = "SELECT cities.id, cities.name, states.name FROM states INNER JOIN \
    cities ON cities.state_id = states.id ORDER BY cities.id"

    # Execute SQL query
    cursor.execute(sql)

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print elements
    for element in results:
        print(element)

    cursor.close()

    # Disconnect from server
    db.close()
