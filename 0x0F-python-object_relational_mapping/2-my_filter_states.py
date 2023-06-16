#!/usr/bin/python3
"""script takes in argument and displays values in states of hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    connct = MySQLdb.connect(host="localhost", port=3306, user="root",
                             passwd="root", db=sys.argv[3], charset="utf8")
    cur = connct.cursor()
    cur.execute("SELECT * FROM states \
    WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close
    connct.close
