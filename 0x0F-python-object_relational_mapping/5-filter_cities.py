#!/usr/bin/python3
"""script to select all cities in a given state"""
from sys import argv as sysargv◘
import MySQLdb as sqldb


def get_state_cities():
    """selects all cities from the state passed as an argument"""
    script, user, passwd, db_name, state = sysargv
    db = sqldb.connect(host='localhost', port=3306,
                       user=user, passwd=passwd, db=db_name)
    c = db.cursor()
    query = "SELECT cities.name FROM cities\
             WHERE cities.state_id=(\
             SELECT id FROM states\
             WHERE name='{}')\
             ORDER BY cities.id".format(state)
    c.execute(query)
    states = c.fetchall()
    for state in states:
        print(state[0], end='')
        if states.index(state) != len(states) - 1:
            print(", ", end='')
    print('')


if __name__ == "__main__":
    get_state_cities()
