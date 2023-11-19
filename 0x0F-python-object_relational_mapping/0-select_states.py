#!/usr/bin/python3

"""List all the states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':

    user = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306, user=user, passwd=password, db=dbname)

    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY states.id ASC;')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
