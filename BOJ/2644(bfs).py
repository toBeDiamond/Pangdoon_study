from collections import deque

def bfs(S, R):                                   # 시작점 S와 깊이를 담아줄 R을 인자로 넣어준다.

    while Q:                                     # Q가 있을 때 까지 돌린다.
        tmp = Q.popleft()                        # tmp로 Q를 빼내어준다 이때 S, R 두개의 값이 나온다.
        if tmp[0] == b:                          # 만약 찾고자 하는 b의 값에 도달했다면
            return tmp[1]                        # tmp[1] 즉, 깊이인 R을 도출해낸다.
        for i in arr[tmp[0]]:                    # 일단 인접리스트를 돌아준다.
            if visited[i] == 0:                  # visited 가 0이라면 체킹을 해주고 Q에 지점과 깊이를 같이 넣어준다.
                visited[i] = 1
                Q.append((i,(tmp[1]+1)))
    return -1            # 만일 Q를 다돌았음에도 불구하고 도착지에 도착하지 못하였으면 -1 값을 뱉어낸다.




N = int(input())
a, b = map(int, input().split())
m = int(input())
Q = deque()
arr = [[] for _ in range(N+1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


visited = [0] * (N+1)
Q.append((a, 0))
visited[a] = 1

print(bfs(a, 0))


