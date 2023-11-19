#!/usr/bin/python3
"""
"""

import sys
import MySQLdb

if __name__ == "__main__":
    da = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    con = da.cursor()
    con.execute("SELECT cities.id, cities.name, states.name, \
                 FROM states INNER JOIN cities ON state_id = \
                 states.id ORDER BY cities.id;")
    for row in con.fetchall():
        print(row)
    con.close()
    da.close()
