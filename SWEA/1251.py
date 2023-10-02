def prim(start):  # prim 함수를 쓴다 (시작점 넣기)
    Earth[start] = 0  # 우선 시작점은 0 으로 

    for _ in range(N):  # Min 값 초기화 시켜주기 위해서
        Min_Earth = 1e12  # Min 값 주기
        for i in range(N):  # 섬개수만큼 for 문 돌기
            if visited[i] == 0 and Min_Earth > Earth[i]: # 방문하지 않았고, 최소값 갱신
                Min_Earth = Earth[i]
                v = i         # 제일 최소값을 가진 곳이 체킹되면
        visited[v] = 1        # 방문해주기 ( v 값은 밑에 인접행렬에서 사용하기위해 빼둠)

        for w in range(N):     # 포문을 돌면서  
            if visited[w] == 0:     # 방문하지 않은 곳이라면 더 작은 값으로 업데이트
                Earth[w] = min(Earth[w], island[v][w])

    
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):  # 개수 만큼 돌려주기
    N = int(input())  # 섬의 개수
    X = list(map(int, input().split()))  # X 좌표 섬 리스트
    Y = list(map(int, input().split()))  # Y 좌표 섬 리스트
    E = float(input())  # 세율 구하기

    island = [[0] * N for _ in range(N)]  # 섬들의 인접행렬 리스트
    for i in range(N):  # 인접행렬 리스트 만들어주기
        for j in range(N):
            island[i][j] = island[j][i] = E * ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)  # 문제 조건에 맞게 만들어 주기
            # 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(E * L^2)만큼 지불

    visited = [0] * N  # 방문체크
    Earth = [1e12] * N  # 환겸 부담금 처음에 크게 만들어놓기

    prim(0)  # 함수 실행

    ans = round(sum(Earth))

    print(f'#{test_case} {ans}')

