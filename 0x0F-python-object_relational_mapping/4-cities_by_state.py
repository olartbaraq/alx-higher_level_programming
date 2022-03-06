#!/usr/bin/python3
"""module that lists all cities from a database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    mydb = MySQLdb.connect(user=username, passwd=password, db=db_name)
    cur = mydb.cursor()
    text1 = "SELECT cities.id, cities.name, states.name FROM cities"
    text2 = "LEFT JOIN states ON cities.state_id=states.id ORDER BY cities.id"
    text_concat = text1 + ' ' + text2
    cur.execute(text_concat)

    cities = cur.fetchall()

    for city in cities:
        print(city)
