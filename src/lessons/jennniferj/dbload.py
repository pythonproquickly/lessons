import sqlalchemy
import csv

TABLE = "driver"

with open("/home/andy/data/drivers_s.csv", "r") as f:
    contents = f.readlines()

heading = "".join(contents[0])

engine = sqlalchemy.create_engine("sqlite:///dbms.db")
with engine.connect() as conn:
    sql = sqlalchemy.text(f"drop table if exists {TABLE}")
    results = conn.execute(sql)
    sql = sqlalchemy.text(f" create table {TABLE} ({heading})")
    results = conn.execute(sql)

    for line in contents[1:]:
        new_line = ""
        for word in line.split(","):
            if len(word) > 0 and word[0] == '"':
                delim = ""
            else:
                delim = "'"
            new_line = new_line + delim + word.strip() + delim + ", "
        sql = sqlalchemy.text(
            f"insert into {TABLE} ({heading}) values ({new_line[:-2]});"
        )
        results = conn.execute(sql)

    with open("/home/andy/data/new_drivers_s.csv", "w") as csvfile:
        csvfile.write(heading)
        outcsv = csv.writer(csvfile)
        sql = sqlalchemy.text(f"select * from {TABLE}")
        results = conn.execute(sql)
        for record in results:
            outcsv.writerow(record)
