'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''
import sys; sys.stdin=open('./11879.py', encoding='utf-8'); qwdsad=input()

def dfs(i, j):      # dfs함수를 정의 (필요한 파라미터는 i, j)
    global flag     # flag 글로벌 선언 > 미로 출구를 찾았나 못 찾았나를 알려줌
    visited[i][j] = 1
    if arr[i][j] == 3:    # 만약에 arr[si][sj]가 3이라면 flag를 1로 바꾸고 return 해준다.
        flag = 1
        return

    di = [0, 1, 0, -1]      # 4방향
    dj = [1, 0, -1, 0]
    for k in range(4):      # 4방향으로 돈다.
        ni = i + di[k]      # 4방향으로 돌았을때 ni로 그만큼 범위지정
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:     # 그 범위가 NxN을 벗어나면 안됌.
            if visited[ni][nj] == 0 and arr[ni][nj] != 1:   # visited 가 0인 곳이고 arr[ni][nj]가 0 혹은 3인 곳만 간다.
                dfs(ni, nj)     # 그렇게 다시 함수를 불러온다. / 만일 함수를 불렀을 때 3이라면? 1로 바꾸고 return

T = int(input())    # 테스트케이스 몇개인지 받아준다.
for test_case in range(1, T + 1):    # 테스트케이스만큼 돌려준다.
    N = int(input())    # NxN을 확인한다.
    arr = [list(map(int, input())) for _ in range(N)]   #한꺼 번에 받아야 하는 배열 양
    visited = [[0] * N for _ in range(N)]   # 방문체크를 위해서 확인해준다.
    flag = 0    # 있는지 없는지 확인을 해주는 flag 설정

    for i in range(N):      # NxN 에서 2가 어디있는지 찾아준다.
        for j in range(N):
            if arr[i][j] == 2: # 시작점을 찾았다면
                dfs(i, j) # 시작점인 i j 를 기준으로 dfs 시작
    print(f'#{test_case} {flag}')

    ##########################################################################

    def dfs(i, j):  # dfs함수를 정의 (필요한 파라미터는 i, j)
        global flag  # flag 글로벌 선언
        visited[i][j] = 1  # 방문체크
        if arr[i][j] == 3:  # 도착지에 도착했으면 flag를 1로 바꾸고 return 해준다.
            flag = 1
            return

        di = [0, 1, 0, -1]  # 4방향
        dj = [1, 0, -1, 0]
        for k in range(4):  # 4방향으로 돈다. 우, 하, 좌, 상 순으로 돈다.
            ni = i + di[k]  # 4방향으로 돌았을때 ni, nj로 그만큼 범위지정
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:  # 그 범위가 NxN을 벗어나면 안 됨.
                if visited[ni][nj] == 0 and arr[ni][nj] != 1:  # 방문한 적이 없음 and 갈 수 있는 곳임 (=벽이 아님)
                    dfs(ni, nj)  # 그렇게 다시 함수를 불러온다. / 만일 함수를 불렀을때 3이라면? 1로 바꾸고 return


    T = int(input())  # 테스트케이스 몇개인지 받아준다.
    for test_case in range(1, T + 1):  # 테스트케이스만큼 돌려준다.
        N = int(input())  # NxN을 확인한다.
        arr = [list(map(int, input())) for _ in range(N)]  # 배열 저장
        visited = [[0] * N for _ in range(N)]  # 방문체크를 위해서 확인해준다.
        flag = 0  # 있는지 없는지 확인을 해주는 flag 설정
        si = 0  # 시작점 i행
        sj = 0  # 시작점 j열
        for i in range(N):  # NxN 에서 2가 어디있는지 찾아준다.
            for j in range(N):
                if arr[i][j] == 2:
                    si = i  # 그렇게 찾는 i를 시작점으로 지정
                    sj = j

                    dfs(si, sj)
        print(f'#{test_case} {flag}')