from collections import deque
import sys

def bfs(start, jump):
    while Q:                                            # Q가 돌아가는 동안
        tmp = Q.popleft()                               # tmp 에서 빼내준다.
        if tmp[0] == N-1:                               # 만일 마지막 까지 도달했다면
            return tmp[1]                               # 그 깊이, 점프횟수를 뱉어낸다.

        for i in range(1, arr[tmp[0]] + 1):             # 1(자기자신은 다시 안가도되므로 다음 한칸부터), 시작점과 연결된 개수만큼 + 1
            next_start = tmp[0] + i                     # 다음 시작점은 , 방금 시작한 것 + i 이다
            if next_start not in visited:               # 다음 시작점이 방문한적 없는 곳이라면
                Q.append((next_start, tmp[1] + 1))      # Q 에 넣어준다, 다음 시작할 점과, 점프횟수
                visited.append(next_start)              # 그리고 방문체크를 해준다.

    return -1

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
visited =[]                # 방문 한 장소 나타내주기
Q = deque()                    # deque 로나타내주기
Q.append((0, 0))

print(bfs(0, 0))