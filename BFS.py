
graph={
    '5' : [ '3','7'],
    '3' : [ '2','4'],
    '7' : [ '8'],
    '2' : [],
    '4' : [ '8'],
    '8' : []
}

visited = []
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m,end= " ")
        for n in graph[m]:
            if n not in visited:
                visited.append(n)
                queue.append(n)

bfs(visited,graph,'5')



