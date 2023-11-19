#!/usr/bin/python3
"""
"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    da = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    con = da.cursor()
    con.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC")
    for row in con.fetchall():
        if row[1] == argv[4]:
            print(row)
    con.close()
    da.close()
