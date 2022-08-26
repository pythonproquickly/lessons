import csv
  
# Open file 
with open('/Users/andy/ws/ctpsws-clients/lessons/src/lessons/samuelo/data/log_summary.csv') as f:
    rows = f.readlines()
    print(rows)
    for row in rows:
        if len(row.split('\xFE')) != 4:
            print(row)
        else:
            print(".")