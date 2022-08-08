def dfs(graph, node):
    # node is the starting position
    # graph is the graph in dictionary format
    visited = []
    stack = []

    stack.append(node)
    visited.append(node)

    while stack:
        s = stack.pop()
        print(f"{s=}")
        for x in graph[s][::-1]:
            print(f"{x=}")
            if x not in visited:
                visited.append(x)
                stack.append(x)

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['F'],
    'F':[]
}
dfs(graph,'A')
