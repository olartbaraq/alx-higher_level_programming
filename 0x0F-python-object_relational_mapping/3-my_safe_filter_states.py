#!/usr/bin/python3
"""Script to prevent SQL injection from attackers"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    data_base = MySQLdb.connect(host="localhost", port=3306,
                                user=username, passwd=password, db=db_name)
    cur = data_base.cursor()
    cur.execute("""SELECT * FROM states WHERE name = %s ORDER BY states.id""",
                (state_name, ))
    state_id = cur.fetchall()
    for states_no in state_id:
        print(states_no)
