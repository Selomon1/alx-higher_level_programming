#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa where name matches
the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    da = MySQLdb.connect(host="localhost", port=3306, user=sys.srgv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    con = da.cursor()
    con.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".
    format(sys.argv[4]))
    for row in con.fetchall():
        if row[1] == sys.argv[4]:
            print(row)
    con.close()
    da.close()
