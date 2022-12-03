def exec_query1(date, identifier):
    # function that performs the query and return results as a dictionary
    # eg:
    # query uses date and identifier
    # query data returned as lists
    column_names = ['deal', 'date', 'etc_q1']
    query_data = [
        ['XXX11', 'etcq1_1'],
        ['XXX12', 'etcq1_2']
    ]
    # add date and convert to list of dictionaries
    results = []
    for query_row in query_data:
        query_row.insert(1, date)
        results.append(dict(zip(column_names, query_row)))
    return results


def exec_query2(date, identifier):
    # see exec_query1 above
    column_names = ['deal', 'date', 'etc_q2']
    query_data = [
        ['XXX11', 'etcq2_1'],
        ['XXX12', 'etcq2_2']
    ]
    results = []
    for query_row in query_data:
        query_row.insert(1, date)
        results.append(dict(zip(column_names, query_row)))
    return results


def exec_query3(date, identifier):
    # see exec_query1 above
    column_names = ['deal', 'date', 'etc_q3']
    query_data = [
        ['XXX11', 'etcq3_1'],
        ['XXX12', 'etcq3_2']
    ]
    results = []
    for query_row in query_data:
        query_row.insert(1, date)
        results.append(dict(zip(column_names, query_row)))
    return results


color_csv = [
    ['deal', 'date', 'bloomberg_ticker', 'blah'],
    ['XXX11', '2022/01/12', 'BB-AA-01', 'more stuff a...'],
    ['XXX12', '2022/02/09', 'BB-AA-02', 'more stuff b...'],
]


def main():
    results = []

    for query_select_data in color_csv[1:]:
        results.append(exec_query1(query_select_data[1], query_select_data[2]))
        results.append(exec_query2(query_select_data[1], query_select_data[2]))
        results.append(exec_query3(query_select_data[1], query_select_data[2]))

    final_results = {}
    for source in color_csv[1:]:
        final_results[source[0]] = {}
        final_results[source[0]][color_csv[0][1]] = source[1]

    for result in results:
        for query_result_line in result:
            for key, value in query_result_line.items():
                if key == 'deal':
                    continue
                if final_results[query_result_line['deal']].get(key,
                                                                None) is None:
                    final_results[query_result_line['deal']][key] = ""
                final_results[query_result_line['deal']][key] = value

    headers = ['deal', 'date', 'q1data', 'q2data', 'q3data']
    final = []
    final.append(headers)
    for final_result_key, final_result_value in final_results.items():
        output_line = [final_result_key]
        for inner_key, inner_value in final_result_value.items():
            output_line.append(inner_value)
        final.append(output_line)

    for line in final:
        print(line)


if __name__ == "__main__":
    main()
