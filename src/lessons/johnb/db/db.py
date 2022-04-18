"""
show simplest database operation
"""

import sqlite3

sql_statements = [
    "drop table if exists test",
    "create table test (id, name)",
    "insert into test values (1, 'abc')",
    "insert into test values (2, 'def')",
    "insert into test values (3, 'xyz')",
]

sql = input("which record number?: ")
full_sql = "select id, name from test where id = " + sql
sql_statements.append(full_sql)
print(sql_statements[-1])


def main():
    """ run the sql """
    conn = sqlite3.connect("dbms.db")
    c = conn.cursor()
    [c.execute(statement) for statement in sql_statements[:-1]]
    conn.commit()
    rows = c.execute(sql_statements[-1])
    print(list(rows))
    # rows = c.execute("select id, name from test where id = ?;", (2,))
    # print(list(rows))
    c.close()
    conn.close()


if __name__ == "__main__":
    main()
