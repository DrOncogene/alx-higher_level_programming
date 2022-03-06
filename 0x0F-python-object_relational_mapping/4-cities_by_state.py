#!/usr/bin/python3
"""script to select all entries from the cities table from a db
passed as an argument"""
import MySQLdb as sqldb
from sys import argv as sysargv


def get_cities():
    """selects all cities from the database"""
    script, user, passwd, db_name = sysargv
    db = sqldb.connect(host='localhost', port=3306,
                       user=user, passwd=passwd, db=db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM cities ORDER BY cities.id""")
    states = c.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_cities()
