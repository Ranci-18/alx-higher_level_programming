#!/usr/bin/python3
'''module lists all states from hbtn_0e_0_usa database'''
import MySQLdb
import sys


if __name__=="__main__":
    connect = MySQLdb.connect(host="localhost", port=3306,
                              user="root", passwd="root", db=sys.argv[3],
                              charset="utf8")
    cur = connect.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close
    connect.close
