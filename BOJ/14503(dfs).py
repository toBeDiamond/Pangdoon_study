import sys
sys.setrecursionlimit(10**6)

def dfs(a, b, direct):
    global count

    # 방향에 따라 회전 순서를 변경
    if direct == 0:
        direction = [3, 2, 1, 0]
    elif direct == 1:
        direction = [0, 3, 2, 1]
    elif direct == 2:
        direction = [1, 0, 3, 2]
    else:  # direct == 3
        direction = [2, 1, 0, 3]

    for i in direction:
        ni = a + four_scavenger_di[i]
        nj = b + four_scavenger_dj[i]

        if 0 <= ni < N and 0 <= nj < M:  # 범위 확인
            if room[ni][nj] == 0:
                room[ni][nj] = 2
                count += 1
                dfs(ni, nj, i)
                return

    # 네 방향 모두 청소할 곳이 없으면 후진
    bi = a + back_scavenger_di[direct]
    bj = b + back_scavenger_dj[direct]

    if 0 <= bi < N and 0 <= bj < M and room[bi][bj] != 1:
        dfs(bi, bj, direct)

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
room = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
four_scavenger_di = [-1, 0, 1, 0]  # 북 동 남 서
four_scavenger_dj = [0, 1, 0, -1]  # 0 1 2 3 순서
back_scavenger_di = [1, 0, -1, 0]       # 북 <-> 남 , 서 <-> 동
back_scavenger_dj = [0, -1, 0, 1]       # 0과 2 / 1과 3
count = 1
room[r][c] = 2
dfs(r, c, d)

print(count)