#!/usr/bin/python3
"""Script to select all states with "N" name from database `hbtn_0e_0_usa`"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    data_base = MySQLdb.connect(user=username, passwd=password, db=db_name)
    cur = data_base.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE 'N%' "
                "ORDER BY id ASC")
    table = cur.fetchall()
    for row in table:
        print(row)
    cur.close()
    db.close()
