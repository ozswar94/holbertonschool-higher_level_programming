#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa where name egal name of filed

Arguments:
    mysql username sys.argv[1]
    mysql password sys.argv[2]
    database name sys.argv[3]
    name of filed sys.argv[4]
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    curs = db.cursor()
    curs.execute("""
    SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id
    """.format(sys.argv[4]))
    for row in curs.fetchall():
        print(row)
    curs.close()
    db.close()
