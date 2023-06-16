#!/usr/bin/python3
"""script lists all states with a name starting with N from hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    connct = MySQLdb.connect(host='localhost', port=3306, user='root',
                             passwd='root', db=sys.argv[3], charset='utf8')

    cur = connct.cursor()
    cur.execute("SELECT id,"
                "name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
    cur.close
    connct.close
