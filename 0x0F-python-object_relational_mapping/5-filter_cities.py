#!/usr/bin/python3
"""
Script to list all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

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

    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s;
    """
    cursor.execute(query, (state_name,))

    cities = cursor.fetchone()
    if cities[0]:
        print(cities[0])

    cursor.close()
    db.close()
