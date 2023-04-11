# 6593 상범빌딩

import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

def bfs(z, x, y):
   queue = deque([(z, x, y)])

   while queue:
    z, x, y = queue.popleft()  

    for i in range(6):
        nz = dz[i] + z
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < r and 0 <= ny < c and 0 <= nz < l and visited[nz][nx][ny] == 0 and not graph[nz][nx][ny] == '#':
          visited[nz][nx][ny] = visited[z][x][y] + 1
          if graph[nz][nx][ny] == 'E':
             print(f"Escaped in {visited[nz][nx][ny]} minute(s).")
             return
          queue.append((nz, nx, ny))
    
   print("Trapped!")
             

while True:
  l, r, c = map(int, input().split())

  if l == 0 and r == 0 and c == 0:
     break
  
  visited = [[[0] * c for _ in range(r)] for _ in range(l)]
  graph = []
  for i in range(l):
      floor_temp = []
      for j in range(r):
          temp = list(input().strip())
          if 'S' in temp:
             s_index = [i, j, temp.index('S')]
          floor_temp.append(temp)
      graph.append(floor_temp)
      input()

  bfs(s_index[0], s_index[1], s_index[2])
