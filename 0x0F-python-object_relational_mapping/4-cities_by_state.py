#!/usr/bin/python3
"""  lists all cities"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = conn.cursor()
    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities LEFT JOIN states
                   ON states.id = cities.state_id
                   ORDER BY cities.id ASC""", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
