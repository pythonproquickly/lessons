# PART 3

# Andy: I completed PART 3 a) and everything worked fine,
# I found the shortest path and the number of nodes visited in that path = 7
# But then I did PART 3 b), wrote path = queue.pop(0) and vertex = path[-1] and then it stoped working.
# it is giving me errors line 37 and 62 "unhashable type 'list'".
import pysnooper


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
            if n is node_map.keys():
                node_map[n2].append(n1)
            else:
                node_map[n2] = [n1]

    return node_map


@pysnooper.snoop()
def bfs_shortest_path(graph, start, goal):
    queue = [(start, [start])]

    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        next_node_list = [x for x in graph[vertex] if x not in set(path)]

        for next in next_node_list:
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))


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
    # Andy: I think this needs to be modified but I am not sure how.
    bfs_path_list = list(bfs_shortest_path(graph, start_node, goal_node))

    # write code to print the shortest path and number nodes for BFS
    print("Shortest path:", bfs_path_list)
    print("Number of nodes explored:", len(bfs_path_list))

    #write code to call bfs_shortest_path (graph, start, goal)
    # Andy: I am not sure what I am supposed to do here.


# run the main function
main()
