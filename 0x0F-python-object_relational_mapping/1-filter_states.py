#!/usr/bin/python3
"""script to select all entries from the states table from a db
passed as an argument"""
import MySQLdb as sqldb
from sys import argv as sysargv


def get_N_states():
    """selects all states from the database that starts with N"""
    script, user, passwd, db_name = sysargv
    db = sqldb.connect(host='localhost', port=3306,
                       user=user, passwd=passwd, db=db_name)
    c = db.cursor()
    c.execute("""SELECT * FROM states
              WHERE (states.name LIKE BINARY 'N%')
               ORDER BY states.id""")
    states = c.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_N_states()
