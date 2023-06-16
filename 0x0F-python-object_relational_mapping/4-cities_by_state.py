#!/usr/bin/python3
"""script lists all cities from database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    connct = MySQLdb.connect(host="localhost", port=3306, user="root",
                             passwd="root", db=sys.argv[3], charset="utf8")
    cur = connct.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close
    connct.close
