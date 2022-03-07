#!/usr/bin/python3
"""module that lists all cities from a database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    state_name = "'" + state_name + "'"

    mydb = MySQLdb.connect(user=username, passwd=password, db=db_name)
    cur = mydb.cursor()
    text1 = "SELECT states.id, states.name, cities.name "
    text2 = "FROM cities LEFT JOIN states ON "
    text3 = "cities.state_id = states.id "
    text4 = "WHERE states.name = {:s} ".format(state_name)
    text5 = "ORDER BY cities.id "
    real_sql_query = text1 + text2 + text3 + text4

    cur.execute(real_sql_query)
    cities = cur.fetchall()

    city_argument = ''
    argument_count = 1
    for city in cities:
        if (argument_count != len(cities)):
            city_argument += city[2] + ', '
            argument_count += 1
        else:
            city_argument += city[2]
    print(city_argument)
