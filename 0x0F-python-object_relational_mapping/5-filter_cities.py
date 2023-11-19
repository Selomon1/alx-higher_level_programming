#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of the state using the data base hbtn_0e_4_usa
"""


import sys
from sys import argv
import MySQLdb

if __name__ == "__main__":
    da = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    con = da.cursor()
    con.execute("SELECT * FROM cities JOIN states \
                ON cities.states_id = state.id ORDER BY cities.id")
    [print(", ".join([c[2] for c in con.fetchall() if c[4] == argv[4]]))]
    con.close()
    da.close()
