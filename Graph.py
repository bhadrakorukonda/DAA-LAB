graph = {
    '7' : ['3','5'],
    '3' : ['2', '4'],
    '2' : [],
    '4' : ['8'],
    '8' : [],
    '7' : ['8']
 }           

visited = set()
           
def dfs(visited,graph,node):
    if node not in visited:
           print(node)
           visited.add(node)
           for neighbour in graph[node]:
              dfs(visited, graph, neighbour)
           
#Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '7')