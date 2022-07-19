import pandas as pd
from pipeline import execute_ddl, connect_to_pg


create_table = """
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL,
    survived INT NOT NULL,
    pclass INT NOT NULL,
    name VARCHAR(128) NOT NULL,
    sex VARCHAR(16) NOT NULL,
    age INT NOT NULL,
    sibs_spouses INT NOT NULL,
    parents_children INT NOT NULL,
    fare DECIMAL(6) NOT NULL
)
"""


def generate_insert_statement(df):
    row_strs = []
    for i, row in df.iterrows():
        name = row['Name'].replace("'", "''")
        row_str = f"""({row['Survived']},{row['Pclass']},'{name}','{row['Sex']}',{row['Age']},{row['Siblings/Spouses Aboard']},{row['Parents/Children Aboard']},{row['Fare']})"""
        row_strs.append(row_str)

    base_query = f"""
    INSERT INTO titanic
    (survived, pclass, name, sex, age, sibs_spouses, parents_children, fare)
    VALUES
    {','.join(row_strs)}
    """
    return base_query

if __name__ == '__main__':
    df = pd.read_csv('titanic.csv')
    pg_conn = connect_to_pg()
    execute_ddl(pg_conn, create_table)
    insert_statement = generate_insert_statement(df)
    print(insert_statement)
    execute_ddl(pg_conn, insert_statement)
    pg_conn.commit()
