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
    sql = """
    SELECT cities.name FROM cities INNER JOIN states
    ON cities.states_id=state.id WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    con.execute(sql, (argv[4],))
    rows = con.fetchall()
    print(", ".join(c[0] for c in rows)
    con.close()
    da.close()
