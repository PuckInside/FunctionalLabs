#lab 4

graph = {
  0 : [1, 2, 3],
  1 : [2],
  2 : [4],
  3 : [],
  4 : []
}

def dfs(visited: list, graph: dict, node):
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

    return visited

visited = dfs(list(), graph, 0)
print(visited)