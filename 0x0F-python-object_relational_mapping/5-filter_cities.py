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
    SELECT cities.name FROM cities, states WHERE states.name=%(name_state)s AND
    states.id=cities.state_id ORDER BY cities.id ASC;
    """, {'name_state': sys.argv[4]}
    )
list_result = list(curs.fetchall())
for row in list_result:
    if list_result[-1] != row:
        print(row[0], end=', ')
    else:
        print(row[0])
curs.close()
db.close()
