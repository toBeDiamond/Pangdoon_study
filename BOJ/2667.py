from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
Q = deque()
result = 0
danji = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            cnt = 1
            arr[i][j] = 0
            Q.append((i, j))
            result += 1
            while Q:
                tmp = Q.popleft()
                for k in range(4):
                    ni = tmp[0] + di[k]
                    nj = tmp[1] + dj[k]
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 1:
                        arr[ni][nj] = 0
                        Q.append((ni, nj))
                        cnt += 1
            danji.append(cnt)
danji.sort()
print(result)
for i in danji:
    print(i)


