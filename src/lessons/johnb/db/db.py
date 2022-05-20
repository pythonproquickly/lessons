"""
show simplest database operation
"""
from loguru import logger

logger.DEBUG("jjjjjj")
logger.INFO("KKK")
import sqlite3

sql_statements = [
    "drop table if exists test",
    "create table test (id, name)",
    "insert into test values (1, 'abc')",
    "insert into test values (2, 'def')",
    "insert into test values (3, 'xyz')",
]


def main():
    """run the sql"""
    sql = input("which record number?: ")
    full_sql = "select id, name from test where id = " + sql
    sql_statements.append(full_sql)
    conn = sqlite3.connect("dbms.db")
    c = conn.cursor()
    [c.execute(statement) for statement in sql_statements[:-1]]
    conn.commit()
    """rows = c.execute(sql_statements[-1])
    print(list(rows))
    print(sql_statements[-1])"""
    s = int(sql)
    rows = c.execute("select id, name from test where id = ?;", (s,))
    print(list(rows))
    c.close()
    conn.close()


if __name__ == "__main__":
    main()
