#!/usr/bin/python3
"""
Lists all the states from the given database hbtn_0e_0_usa
"""


import sys
import MySQLdb

if (__name__ == "__main__"):
    da = MySQLdb.connect(host= "localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    con = da.cursor()
    con.execute("SELECT * FROM states ORDER BY id ASC")
    for row in con.fetchall():
        print (row)
    con.close()
    da.close()
