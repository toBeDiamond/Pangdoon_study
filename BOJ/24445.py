from collections import deque
import sys
def bfs():
    global count
    while Q:
        tmp = Q.popleft()
        for j in sorted(board[tmp],reverse=True):
            if visited[j] == 0:
                count += 1
                visited[j] = 1
                result[j] = count
                Q.append(j)



N, M, R = map(int, sys.stdin.readline().rstrip().split())

Q = deque()
visited = [0] * (N+1)
board = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    board[a].append(b)
    board[b].append(a)
result = [0] * (N+1)
count = 1
visited[R] = 1
Q.append(R)
result[R] = count
bfs()

for i in range(1, N+1):
    print(result[i])
