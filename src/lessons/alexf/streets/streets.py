from pathlib import *
path = Path.cwd() / "streets.txt"
with path.open('r') as f:
    dict = {}
    roadnr = 0
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "FID,Fromnode,Tonode" or line == "":
            continue
        roadnr += 1
        line = line.split(",")
        nodes = line[1], line[2]
        for index in range(len(nodes)):
            if nodes[index] not in dict.keys():
                dict[nodes[index]] = 1
            else:
                dict[nodes[index]] += 1

print("Roads loaded: " + str(roadnr))
while True:
    id = input("Enter a node id (-1 to exit): ")
    if id == "-1":
        break
    if id in dict.keys():
        print(f"Degree for node {id} is {dict[id]}")
    else:
        print(f"Degree for node {id} not found")
print("Program finished")

