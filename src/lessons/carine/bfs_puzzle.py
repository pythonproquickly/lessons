# PART 4, A et B

# Andy: I get errors line 48 and 25 (same as for bfs_shortest_path file)


def get_child_boards_list(board, directed=False):
    node_map = {}

    for edge in board:
        if edge[0] not in node_map:
            node_map[edge[0]] = []
        if edge[1] not in node_map[edge[0]]:
            node_map[edge[0]].append(edge[1])
        if not directed:
            if edge[1] not in node_map:
                node_map[edge[1]] = []
            if edge[0] not in node_map[edge[1]]:
                node_map[edge[1]].append(edge[0])

    return node_map


def bfs2(graph, start_board, goal_board):
    queue = [(start_board, [start_board])]

    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        next_node_list = [x for x in graph[vertex] if x not in set(path)]

        for next in next_node_list:
            if next == goal_board:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def main():

    board = [[4, 1, 3], [2, 0, 6], [7, 5, 8]]

    # create your graph data structure from the node_list
    graph = get_child_boards_list(board, directed=False)

    # Breadth First...
    print("\nBreadth First Search-----------")
    start_node = 0
    goal_node = 8

    # get a list of all the paths to goal using BFS
    # this works because of the yield used in the code

    bfs_path_list = list(bfs2(graph, start_node, goal_node))

    # write code to print the shortest path and number nodes for BFS
    print("Shortest path:", bfs_path_list)
    print("Number of nodes explored:", len(bfs_path_list))

    # run the main function


main()
