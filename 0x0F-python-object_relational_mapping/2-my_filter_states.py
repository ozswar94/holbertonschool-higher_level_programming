#!/usr/bin/python3

import sys
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
    )
curs = db.cursor()
curs.execute("SELECT * FROM states WHERE name='{}'".format(sys.argv[4]))
for row in curs.fetchall():
    print(row)
curs.close()
db.close()
