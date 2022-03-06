#!/usr/bin/python3
"""script to select matching entries from the states table from a db
passed as an argument"""
import MySQLdb as sqldb
from sys import argv as sysargv


def get_state():
    """selects all states from the database that matches a given state"""
    script, user, passwd, db_name, state = sysargv
    db = sqldb.connect(host='localhost', port=3306,
                       user=user, passwd=passwd, db=db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM states
             WHERE states.name=%s
             ORDER BY states.id""", (state,))
    states = c.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_state()
