#!/usr/bin/python3
"""
List all the states with a name starting with N (upper letter) from the given
database, hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    da = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    con = da.cursor()
    con.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in con.fetchall():
        if row[1][0] == 'N':
            print(row)
    con.close()
    da.close()
