
import sys
import queue


class Cell:
    def __init__(self, x, y, dist, prev):
        self.x = x
        self.y = y
        self.dist = dist;  # distance to start
        self.prev = prev;  # parent cell in the path

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"


class ShortestPathBetweenCellsBFS:
    # BFS, Time O(n^2), Space O(n^2)
    def shortestPath(self, matrix, start, end):
        sx = start[0]
        sy = start[1]
        dx = end[0]
        dy = end[1]
        # if start or end value is 0, return
        if matrix[sx][sy] == 0 or matrix[dx][dy] == 0:
            print("There is no path.")
            return
        # initialize the cells
        m = len(matrix)
        n = len(matrix[0])
        cells = []
        for i in range(0, m):
            row = []
            for j in range(0, n):
                if matrix[i][j] != 0:
                    row.append(Cell(i, j, sys.maxsize, None))
                else:
                    row.append(None)
            cells.append(row)
            # breadth first search
        queue = []
        src = cells[sx][sy]
        src.dist = 0
        queue.append(src)
        dest = None
        p = queue.pop(0)
        while p != None:
            # find destination
            if p.x == dx and p.y == dy:
                dest = p
                break
                # moving up
            self.visit(cells, queue, p.x - 1, p.y, p)
            # moving left
            self.visit(cells, queue, p.x, p.y - 1, p)
            # moving down
            self.visit(cells, queue, p.x + 1, p.y, p)
            # moving right
            self.visit(cells, queue, p.x, p.y + 1, p)
            if len(queue) > 0:
                p = queue.pop(0)
            else:
                p = None
                # compose the path if path exists
        if dest == None:
            print("there is no path.")
            return
        else:
            path = []
            p = dest
            while p != None:
                path.insert(0, p)
                p = p.prev
            k=0
            for i in path:
                k=k+1
                print(i)
            print(k)

    # function to update cell visiting status, Time O(1), Space O(1)
    def visit(self, cells, queue, x, y, parent):
        # out of boundary
        if x < 0 or x >= len(cells) or y < 0 or y >= len(cells[0]) or cells[x][y] == None:
            return
        # update distance, and previous node
        dist = parent.dist + 1
        p = cells[x][y]
        if dist < p.dist:
            p.dist = dist
            p.prev = parent
            queue.append(p)

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)
"""matrix = [
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 1]]"""
myObj = ShortestPathBetweenCellsBFS()
sx=int(input("Enter the start row possition : "))
sy=int(input("Enter the start Col possition : "))
ex=int(input("Enter the end row possition : "))
ey=int(input("Enter the end Col possition : "))
# case 2, there is path
start1 = [sx, sy]
end1 = [ex, ey]
print("case 2: ")
myObj.shortestPath(matrix, start1, end1)