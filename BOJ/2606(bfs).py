from collections import deque

C = int(input())
N = int(input())
visited = [0] * (C+1)
Q = deque()
arr = [[] for _ in range(C+1)]
for i in range(N):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

Q.append(1)
while Q:
    tmp = Q.popleft()
    if visited[tmp] == 0:
        visited[tmp] = 1
        for i in arr[tmp]:
            if visited[i] == 0:
                Q.append(i)

print(sum(visited)-1)

