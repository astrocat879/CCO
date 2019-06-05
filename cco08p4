from sys import stdin
from collections import deque
a, b = map(int, stdin.readline().split())
grid = stdin.read().split("\n")
groups = []
q = deque([(0, 0)])
vis = [[False for i in range(b)] for j in range(a)]
def bfs(start, visited):
    q = deque([start])
    while q:
        y, x = q.popleft()
        if (y, x) in visited:
            return True
        if vis[y][x]:
            return False
        vis[y][x] = True
        visited.add((y, x))
        if grid[y][x] == "S":
            q.append((y+1, x))
        elif grid[y][x] == "N":
            q.append((y-1, x))
        elif grid[y][x] == "E":
            q.append((y, x+1))
        elif grid[y][x] == "W":
            q.append((y, x-1))


rooms = 0
for i in range(a):
    for j in range(b):
        if not vis[i][j]:
            if bfs((i, j), set()):
                rooms += 1
print(rooms)
#astrocat879 solution
#regular dfs, however the solution is quite trash
#I recommend waiting for N3rdslqyer84 to come up with a genius and groundbreaking solution.
