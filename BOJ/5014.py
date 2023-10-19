from collections import deque                           # deque를 이용해준다.
import sys                                              # input() 빠르게 받기 위해서

def bfs():                                              # bfs 함수 만들기
    visited = [0] * (F + 1)                             # visited 체크
    while Q:                                            # Q가 빌때까지
        tmp = Q.popleft()
        if tmp[0] == G:                                 # 나의 층수와 목표지점이 같으면
            return tmp[1]                               # BFS 의 깊이 값을 가져온다.

        if visited[tmp[0]] == 0:                        # visited == 0 이라면
            visited[tmp[0]] = 1                         # 1로 바꿔주고
            if tmp[0] + U <= F:                         # 나의 층수에서 U 만큼 더 해준다 (건물 높이보단 같거나 작아야 함)
                Q.append((tmp[0]+U, tmp[1]+1))          # 층수를 바꿔주고 깊이 + 1
            if tmp[0] - D >= 1:                         # 나의 층수에서 D만큼 빼준다. (건물 1층보단 같거나 높아야 함)
                Q.append((tmp[0]-D, tmp[1]+1))          # 층수를 바꿔주고 깊이 + 1

    return -1    # while 문을 다돌았는데도 목표지점에 도착하지 못했다면 -1을 뱉어낸다.

F, S, G, U, D = map(int, sys.stdin.readline().split())      # 이번에 알게된 빠르게 받는법 사용
Q = deque()
Q.append((S, 0))
ans = bfs()

if ans == -1:
    print("use the stairs")
else:
    print(ans)
