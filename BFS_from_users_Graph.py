no_of_vertex=int(input("Enter the no of vertex "))
graph={}

for i in range(no_of_vertex):
    vertex=input("Enter the vertex ")
    graph[vertex]=list()
    flag = True
    while flag:
        child=input(f"Enter the {vertex}'s child (enter 0 if haven't) : ")
        if child!='0':
            graph[vertex].append(child)
        else:
            flag=False
print(graph)
visited = []
queue = []
def BFS(visited,graph,node):

    visited.append(node)
    queue.append(node)
    while queue:
        m=queue.pop(0)
        print(m, " ")
        for n in graph[m]:
            if n not in visited:
                queue.append(n)
                visited.append(n)



print("Printing dfs")
start=input("From Where u want to start ")
BFS(visited,graph,start)