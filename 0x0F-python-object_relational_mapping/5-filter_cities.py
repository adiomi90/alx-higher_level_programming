#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all cities
   of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    state = sys.argv[4]
    cur.execute("SELECT cities.name FROM cities INNER JOIN states\
                 ON cities.state_id = states.id WHERE states.name = %s\
                 ORDER BY cities.id ASC", (state,))
    rows = cur.fetchall()
    result  = []
    for row in rows:
        result.append(row[0])
    print(', '.join(result))
    cur.close()
    db.close()
