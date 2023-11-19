#!/usr/bin/python3

"""List all the states from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
  import MySQLdb
  import sys
  user = sys.argv[1]
  password = sys.argv[2]
  dbname= sys.arv[3]

  db = MySQLdb.connect(host="localhost", port=3306,
                       user=user, passwd=password,db=dbname)

  cur = db.cursor()
  r.execute("SELECT * FROM states ORDER BY states.id ASC;")
  rows = cur.fetchall()
  for row in rows:
    print(row)
  cur.close()
  db.close()
