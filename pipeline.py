import psycopg2
from sqlite_example import connect_to_sqlite
import queries
from pprint import pprint


dbname = 'pbxkhceu'
user = 'pbxkhceu'
host = 'castor.db.elephantsql.com'
password = 'nTxHJyQCN347esaR4eC94WOnKz3gnQNW'


def connect_to_pg():
    return psycopg2.connect(dbname=dbname, user=user, host=host, password=password)


def execute_query(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def execute_ddl(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)


def generate_insert_string(character_data):
    row_strings = []
    for row in character_data:
        row_string = str(row)
        row_strings.append(row_string)
    query = f"""
    INSERT INTO characters
    (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES
    {','.join(row_strings)}
    """
    return query



if __name__ == '__main__':
    # connect to sqlite
    sqlite_conn = connect_to_sqlite()
    # query character table
    character_data = execute_query(sqlite_conn, queries.select_all_characters)
    # connect to pg
    pg_conn = connect_to_pg()
    # create the character table
    execute_ddl(pg_conn, queries.create_character_table)
    # format character data
    insert_statement = generate_insert_string(character_data)
    # insert character data
    execute_ddl(pg_conn, insert_statement)
    pg_conn.commit()
