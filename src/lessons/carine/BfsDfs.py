# HW2  - Compare BFS DFS search algorithms

# PART 2
# todo: 0. replace the function build_graph_as_dict with your code
# todo: 1. add code to count number of nodes visited for both bfs and dfs
#            hint: define global variables
# todo: 2. Write code for bfs_shortest_path (graph, start, goal) and
#         display shortest path and number nodes visited. Modify the BFS
#         algorithm so that only the path is placed on the queue.

# Andy: It is working, but for DFS, it is only giving me one path
# and I guess I am supposed to get more, as the prof is asking us to do a table

# showing the number of nodes explored for BFS and DFS
import pysnooper


@pysnooper.snoop()
def build_graph_as_dict(node_list, directed=False):
    # return a Python Dict with node as key and value = list of
    # children

    node_map = {}

    # add your code

    for tup in node_list:
        n1, n2 = tup
        if n1 in node_map.keys():
            node_map[n1].append(n2)
        else:
            node_map[n1] = [n2]

        if not directed:
            if n2 is node_map.keys():
                node_map[n2].append(n1)
            else:
                node_map[n2] = [n1]
    print(node_map)
    return node_map


def bfs_all_paths(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)
        next_node_list = [x for x in graph[vertex] if x not in set(path)]

        for next in next_node_list:
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def bfs_shortest_path(graph, start, goal):
    # write code so that the shortest path is returned
    # without visiting all the nodes. Your queue should contain
    # only the path, not (vertex, path). Obtain the vertex directly
    # from the path
    queue = [(start, [start])]

    while queue:
        (vertex, path) = queue.pop(0)
        next_node_list = [x for x in graph[vertex] if x not in set(path)]

        for next in next_node_list:
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def dfs_all_paths(graph, start, goal):

    stack = [(start, [start])]

    while stack:
        # note pop()  returns and removes the LAST value in list
        (vertex, path) = stack.pop()
        next_node_list = [x for x in graph[vertex] if x not in set(path)]
        for next in next_node_list:
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# def dfs_shortest_path(graph, start, goal):
#     stack = [(start, [start])]
#
#     while stack:
#         # note pop()  returns and removes the LAST value in list
#         (vertex, path) = stack.pop()
#         next_node_list = [x for x in graph[vertex] if x not in set(path)]
#         for next in next_node_list:
#             if next == goal:
#                 return path + [next]
#             else:
#                 stack.append((next, path + [next]))


# main - runs both DFS and BFS a graph generated from the node_list
def main():

    node_list = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('F', 'G'),
                 ('B', 'F'), ('G', 'E'), ('E', 'K'), ('K', 'L'), ('L', 'M'),
                 ('M', 'C'), ('L', 'J')]

    # create your graph data structure from the node_list
    graph = build_graph_as_dict(node_list, directed=False)

    # Breadth First...
    print("\nBreadth First Search-----------")
    start_node = 'A'
    goal_node = 'E'

    # get a list of all the paths to goal using BFS
    # this works because of the yield used in the code
    bfs_path_list = list(bfs_all_paths(graph, start_node, goal_node))

    # write code to print the shortest path and number nodes for BFS
    print("Shortest path:", bfs_path_list[0])
    print("Number of nodes explored:", len(bfs_path_list[0]))

    # Depth First...
    print("\n\nDepth First Search--------------")

    dfs_path_list = list(dfs_all_paths(graph, start_node, goal_node))

    # write code to call bfs_shortest_path (graph, start, goal)

    # print the shortest path and number nodes for DFS
    print("Shortest path:", dfs_path_list[0])
    print("Number of nodes explored:", len(dfs_path_list[0]))


# run the main function
main()
