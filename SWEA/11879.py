import sys
sys.stdin = open("11879.txt")

def dfs(i, j):
    global flag
    if arr[i][j] == 3:
        flag = 1
        return

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    visited[i][j] = 1  # 방문체크
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == 0 and (arr[ni][nj] == 0 or arr[ni][nj] == 3):
                dfs(ni, nj)


T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    flag = 0
    si = 0
    sj = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
                break

    dfs(si, sj)
    print(f'#{test_case} {flag}')
