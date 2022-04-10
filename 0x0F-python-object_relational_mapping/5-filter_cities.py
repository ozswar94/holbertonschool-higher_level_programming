#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_0_usa
fix injection

Arguments:
    mysql username sys.argv[1]
    mysql password sys.argv[2]
    database name sys.argv[3]
    state name sys.argv[4]
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
    curs.execute(
        """
        SELECT cities.name
        FROM cities INNER JOIN states
        ON cities.state_id = states.id WHERE states.name = %(name_state)s
        ORDER BY cities.id
        """, {'name_state': sys.argv[4]}
        )
    rows = curs.fetchall()
    for i in range(len(rows)):
        print(rows[i][0], end=", " if i + 1 < len(rows) else "")
    print("")
    curs.close()
    db.close()
