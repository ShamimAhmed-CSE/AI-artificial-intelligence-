from queue import Queue
def bfs(m,st,end):
    v=[False]*len(m)
    q=Queue()
    p={st:[st]}
    q.put(st)
    v[st]=True

    while not q.empty():
        n=q.get()

        if n==end:
            return p[n]
        for ng in range(len(m)):
            if m[n][ng] != 0 and not v[ng]:
                v[ng]=True
                p[ng]=p[n]+[ng]
                q.put(ng)

matrix = [[0,1,1,1,0],
          [1,0,0,0,1],
          [1,0,0,0,0],
          [1,0,0,0,0],
          [0,1,0,0,0]]

m=[]

R=int(input("Enter the raw: "))

for i in range(R):
    a = []
    for j in range(R):
        a.append(int(input()))
    m.append(a)
print(m)
st=int(input("Enter the starting num: "))
end=int(input("Enter the ending num: "))
stp=bfs(m,st,end)
if stp:
    print(f"{stp}")
