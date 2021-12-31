def find(query, data):
    selects = query['select']
    displays = query['display']
    for number, line in enumerate(data):
        dictified_line = dictify(line)
        match = False
        for column in selects:
            if selects == ["Y"]:
                match = True
                break
            elif column[0] in dictified_line:
                select_column = column[0]
                select_condition = column[2]
                select_value = column[4:]
                if select_condition:
                    for key, value in dictified_line.items():
                        match = False
                        if select_condition == "=":
                            # print(key, value)
                            if select_column == key and select_value == value:
                                match = True
                        elif select_condition == ">":
                            # print(key, value)
                            if select_column == key and value > select_value:
                                match = True
                        elif select_condition == "<":
                            if select_column == key and value < select_value:
                                match = True
                        """if not match:
                            break"""

                        """if match:  # debug only
                            print(
                                f"MATCH {select_column} : {select_value} from {dictified_line}")
                            print(select_column + ": " + select_value,
                                  select_condition,
                                  dictified_line)"""

        print_line = {}
        if match:
            sort_needed = query.get('sort', '')
            if displays != ['Z']:
                # print(number + 1, "SPECIFIC COLS", dictified_line, displays)
                for key, value in dictified_line.items():
                    for column in ''.join(displays).replace(" ", ""):
                        if key == column:
                            print_line[key] = value
                if print_line != {}:
                    print_line["A"] = f"{str(number + 1000)}[1:]]"
                    """if sort_needed != '':
                        print_line = sort(sort_needed, print_line)"""
                    print(print_line)

            else:
                # print(number + 1, "ALL COLS", dictified_line, displays)
                for key, value in dictified_line.items():
                    print_line[key] = value
                if print_line != {}:
                    """if sort_needed != []:
                        print_line["A"] = f"{str(number + 1000)[1:]}]"
                        for sort_option in sort_needed:
                            print_line = sort(sort_option, print_line)
                    else:"""
                    print_line["A"] = f"{str(number + 1000)[1:]}]"
                    result = ""
            for key, value in print_line.items():
                result += key + ": " + result
            print(print_line)


def sort(sort_type, source):
    destination = {}
    if sort_type[-2:] == '-1':
        for column in sorted(source, key=source.get, reverse=True):
            destination[column] = source[column]
    else:
        for column in sorted(source, key=source.get):
            destination[column] = source[column]
    return destination


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


with open('data.txt') as f:
    data = f.read().splitlines()

queries = {}
query_num = 0
with open('final.txt') as f:
    read_ahead_in_sort = False
    while True:
        if not read_ahead_in_sort:
            line = f.readline().strip()
        else:
            read_ahead_in_sort = False
        if len(line) == 0:
            break
        # print(line)
        if line == "FIND":
            query_num += 1
            queries[query_num] = {}
            queries[query_num]['select'] = []
            queries[query_num]['display'] = []
            # queries[query_num]['type'] = 'FIND'
            line = f.readline().strip()
            if line == "Y":
                queries[query_num]['select'].append(line)
                line = f.readline().strip()
            while line[2] in "<>=":
                queries[query_num]['select'].append(line)
                line = f.readline().strip()
            queries[query_num]['display'].append(
                line[:-1].replace(';', '').strip())

        elif line == "SORT":
            """query_num += 1
            line = f.readline().strip()
            queries[query_num] = {}"""
            line = f.readline().strip()
            queries[query_num]['sort'] = []
            queries[query_num]['sort'].append(line.replace(";", "").strip())
            line = f.readline().strip()
            if line == "SORT":
                line = f.readline().strip()
                queries[query_num]['sort'].append(
                    line.replace(";", "").strip())
            else:
                read_ahead_in_sort = True
        else:
            query_num += 1
            print(f"Query type of {line} invalid for query # {query_num}")
            line = f.readline()

for query_number, query in queries.items():
    print(query_number, query)

for query_number, query in queries.items():
    # if query['type'] == "FIND":
    find(query, data)
    """elif query['type'] == "SORT":
        sort(query, data)"""
