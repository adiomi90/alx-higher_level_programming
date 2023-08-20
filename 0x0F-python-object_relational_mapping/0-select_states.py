#!/usr/bin/python3

if __name == "__main__":
    import MySQLdb
    import sys

    db_connection = MySQLdb.connect(host="localhost", port=3306,
            username=sys.argv[1], password=sys.argv[2],
            db=sys.argv[3])
    my_database = db_connection.cursor()
    my_database.execute("SELECT * FROM states ORDER BY states.id ASC;")

    output = my_database.fetchall()
    for row in output:
        print(output)
