#!/usr/bin/python3
"""
list table
"""
import sys
import MySQLdb

if __name__ = '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id ASC")
    for row in curs.fetchall():
        print(row)
    curs.close()
    db.close()
