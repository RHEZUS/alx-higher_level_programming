#!/usr/bin/python3
import MySQLdb
import sys
"""  lists all states from the database hbtn_0e_0_usa """


if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', port=3306, user = sys.argv[1],
                           password = sys.argv[2], db = sys.argv[3], charset = 'utf8')
    cur = conn.cursor()

    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    conn.close()
