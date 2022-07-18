import sqlite3
from pprint import pprint
import queries


def connect_to_sqlite(db_name='rpg_db.sqlite3'):
    # Connect to the db
    return sqlite3.connect(db_name)


def execute_query(conn, query):
    # Make a cursor
    cursor = conn.cursor()
    # execute query
    cursor.execute(query)
    # pull the results from the cursor
    return cursor.fetchall()


if __name__ == '__main__':
    # query = 'select * from charactercreator_character'
    conn = connect_to_sqlite()
    results = execute_query(conn, queries.select_all_characters)
    pprint(results)