#!/usr/bin/python3
"""script to select all entries from the states table from a db
passed as an argument"""
import MySQLdb as sqldb
from sys import argv as sysargv


def get_state():
    """selects all states from the database that starts with N"""
    script, user, passwd, db_name, state = sysargv
    db = sqldb.connect(host='localhost',
                       user=user, passwd=passwd, db=db_name)
    c = db.cursor()
    query = f"SELECT * FROM states\
             WHERE states.name='{state}'\
             ORDER BY states.id"
    c.execute(query)
    states = c.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_state()
