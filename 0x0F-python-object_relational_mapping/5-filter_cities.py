#!/usr/bin/python3
""" Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa """

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

    # Execute SQL query
    cursor.execute("SELECT cities.name FROM states INNER JOIN \
    cities ON cities.state_id = states.id WHERE states.name = %s", (argv[4],))

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print elements

    print(", ".join(element[0] for element in results))

    cursor.close()

    # Disconnect from server
    db.close()
