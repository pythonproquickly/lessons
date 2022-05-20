def match_condition(key, value, select_condition, select_column, select_value):
    match = False
    if select_condition == "=":
        if select_column == key and select_value == value:
            match = True
        else:
            match = False
    elif select_condition == ">":
        if select_column == key and value > select_value:
            match = True
        else:
            match = False
    elif select_condition == "<":
        if select_column == key and value < select_value:
            match = True
        else:
            match = False
    return match


def find(query, data):
    # y is all records with the columns in them
    # search is all records independently
    selects = query["select"]
    displays = query["display"]
    for number, line in enumerate(data):
        line = line.strip()
        dictified_line = dictify(line)
        match = False
        """print(number + 1, line, selects[0][0] in dictified_line, selects[0][
            0], dictified_line, selects, selects == ["Y"])"""
        for column in selects:
            """print(f"{column=}")
            print(f"{column[0]=}, {dictified_line.keys()=}")
            print(f"{column[0] in dictified_line=}")"""
            if selects == ["Y"]:
                match = True
                break
            elif column[0] in dictified_line:
                select_column = column[0]
                select_condition = column[2]
                select_value = column[4:]
                """print(
                    f"H, {select_condition=},{select_column=},{select_value=}")"""
                if select_condition:
                    for key, value in dictified_line.items():
                        if key != select_column:
                            continue
                        match = match_condition(
                            key, value, select_condition, select_column, select_value
                        )
                        """print(match, key, value,
                              select_condition,
                              select_column,
                              select_value)"""
                        if not match:
                            break

        print_line = ""
        """print("Z", displays == ['Z'], match)"""
        if match:
            if displays != ["Z"]:
                # print(number + 1, "SPECIFIC COLS", dictified_line, displays)
                for key, value in dictified_line.items():
                    for column in "".join(displays).replace(" ", ""):
                        if key == column:
                            print_line += f"{key}: {value} "
                if print_line != "":
                    print_line = f"A: {str(number + 1001)[1:]} " + print_line
                    print(print_line)

            else:
                # print(number + 1, "ALL COLS", dictified_line, displays)
                for key, value in dictified_line.items():
                    print_line += f"{key}: {value} "
                if print_line != "":
                    print_line = f"A: {str(number + 1001)[1:]} " + print_line
                    print(print_line)


def sort(sort_type, source):
    column = sort_type["sort"][0]
    sort_type_code = int(sort_type["sort"][3:].strip())
    data_to_sort = []
    for number, line in enumerate(source):
        if column in line:
            line = f"A: {str(number + 1001)[1:]} " + line
            data_to_sort.append(line)
        line = ""
    if sort_type_code == 1:
        print("ASCENDING SORT")
        for row in sorted(data_to_sort):
            print(row)
    else:
        print("DESCENDING SORT")
        for row in sorted(data_to_sort, reverse=True):
            print(row)
    print("end of sort")


def dictify(data_with_colons):
    trimmed = data_with_colons.replace(": ", ":")
    trimmed = trimmed.split(" ")
    results = dict()
    for field in trimmed:
        if len(field) == 0:
            continue
        field = field.strip()
        results[field[0]] = field[2:]
    return results


with open("data.txt") as f:
    data = f.read().splitlines()
"""for datum in data:
    print(datum)
exit()"""
queries = {}
query_num = 0
with open("final.txt") as f:
    while True:
        line = f.readline().strip()
        if len(line) == 0:
            print("Blank line in file")
            break
        # print(line)
        if line == "FIND":
            query_num += 1
            queries[query_num] = {}
            queries[query_num]["select"] = []
            queries[query_num]["display"] = []
            queries[query_num]["type"] = "FIND"
            line = f.readline().strip()
            if line == "Y":
                queries[query_num]["select"].append(line)
                line = f.readline().strip()
            while line[2] in "<>=":
                queries[query_num]["select"].append(line)
                line = f.readline().strip()
            queries[query_num]["display"].append(line[:-1].replace(";", "").strip())

        elif line == "SORT":
            query_num += 1
            queries[query_num] = {}
            queries[query_num]["type"] = "SORT"
            line = f.readline().strip()
            queries[query_num]["sort"] = line.replace(";", "")

        else:
            query_num += 1
            queries[query_num] = {}
            queries[query_num]["type"] = "ERROR"
            print(f"Query type of {line} invalid for query # {query_num}")
            line = f.readline()
"""for key, query in queries.items():
    print(key, query)
exit()"""
for query_number, query in queries.items():
    # print(query_number, query)
    if query["type"] == "FIND":
        find(query, data)
    elif query["type"] == "SORT":
        sort(query, data)
