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
    query = "SELECT * FROM states\
             WHERE states.name='{}'\
             ORDER BY states.id".format(state)
    c.execute(query)
    states = c.fetchall()
    for state in states:
        print(state)


if __name__ == "__main__":
    get_state()
