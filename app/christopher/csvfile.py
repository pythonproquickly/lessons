import csv
with open('Emp_Info.csv', 'r') as file:
    reader = csv.reader(file)
    for each_row in reader:
        print(each_row)

fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]

filename = "university_records.csv"

use_headers = True

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    if use_headers:
        csvwriter.writerow(fields)
    csvwriter.writerows(rows)
