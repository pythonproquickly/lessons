import pandas as pd
import sqlite3

"""df = pandas.read_csv(csvfile)
df.to_sql(table_name, conn, if_exists='append', index=False, sep=',')"""

sql_statements = (
    "drop table if exists test",
    "create table test (id, name)",
    "insert into test values (1, 'abc')",
    "insert into test values (2, 'def')",
    "insert into test values (3, 'xyz')",
    "select id, name from test",
)


def main():
    """ run the sql """
    conn = sqlite3.connect("dbms.db")
    c = conn.cursor()
    [c.execute(statement) for statement in sql_statements]
    conn.commit()
    rows = c.fetchall()
    print(rows)
    c.close()
    conn.close()


if __name__ == "__main__":
    main()