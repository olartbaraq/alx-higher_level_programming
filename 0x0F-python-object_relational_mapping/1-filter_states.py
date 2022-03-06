#!/usr/bin/python3
"""Script to select all states with "N" name from database `hbtn_0e_0_usa`"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    data_base = MySQLdb.connect(host="localhost", port=3306,
                                user=username, passwd=password, db=db_name)
    cur = data_base.cursor()
    cur.execute("""SELECT * FROM states ORDER BY states.id""")
    table = cur.fetchall()
    for row in table:
        if row[1].startswith("N"):
            print(row)
