#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of the state using the data base hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    da = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3]), charset="utf8")
    con = da.cursor()
    con.execute("SELECT cities.name FROM cities JOIN states \
    ON cities.states_id = state.id where states.name = %s;", (sys.argv[4],))

    print(", ".join(city[0]) for city in con.fetchall())
    con.close()
    da.close()
