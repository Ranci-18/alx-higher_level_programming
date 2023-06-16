#!/usr/bin/python3
"""script lists all cities from database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    connct = MySQLdb.connect(host="localhost", port=3306, user="root",
                             passwd="root", db=sys.argv[3], charset="utf8")
    cur = connct.cursor()
    cur.execute("SELECT cities.name FROM cities \
    JOIN state ON cities.state_id = states.id \
    WHERE states.name LIKE %s ORDER BY cities.id", (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))
    cur.close
    connct.close
