#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of the state using the data base hbtn_0e_4_usa
"""


import sys
from sys import argv
import MySQLdb

if __name__ == "__main__":
    da = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset='utf8')
    con = da.cursor()
    sql = "SELECT cities.name FROM cities WHERE state_id =\
          (SELECT id FROM states WHERE name = %s) ORDER BY cities.id ASC"
    con.execute(sql, (argv[4],))
    rows = con.fetchall()
    for c in rows:
        print(c[0], end='')
        if (c != rows[-1]):
            print(end=', ')
    print()
    con.close()
    da.close()
