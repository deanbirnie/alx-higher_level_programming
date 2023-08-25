#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)

    cursor = db.cursor()

    query = "SELECT * FROM cities ORDER BY id"
    cursor.execute(query)

    cities = cursor.fetchall()
    for city in cities:
        print(city)

    cursor.close()
    db.close()
