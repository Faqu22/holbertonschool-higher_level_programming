#!/usr/bin/python3
"""
    Write a script that lists all states with a name starting with N (upper N)
        from the database hbtn_0e_0_usa.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT states.id, states.name FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1].startswith('N'):
            print(row)
    cur.close()
    db.close()
