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
curs.execute(
    """
    SELECT * FROM cities
    """
    )
for row in curs.fetchall():
    print(row)
curs.close()
db.close()