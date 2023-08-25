T = int(input())                                                # 테스트 케이스 개수
for test_case in range(1, T+1):                                 # 테스트 케이스 개수 만큼 돌려준다.
    N = int(input())                                            # N x N 정하기
    arr = [list(map(int, input())) for _ in range(N)]           # 커다란 배열 받아주기

    count = 0                                                   # 카운트 개수 세아려주기 (변수지정)
    for i in range((N+1)//2):                                   # 홀수로만 주어진다고 하였고 5라면 3까지 7이라면 4까지 지정
        for j in range((N-1)//2-i, (N-1)//2+i+1):               # i가 증가함에 따라 점점 늘어나는 범위
            count += arr[i][j]                                  # 그 범위들을 더해준다

    for i in range((N+1)//2, N):                                # 홀수로만 주어진다고 하였고 5라면 4부터 5까지 7이라면 5부터 7까지 지정
        for j in range(N//2-(N-1-i), N//2+(N-1-i)+1):           # 줄어들게 끔 범위를 만들어주었다.
            count += arr[i][j]                                  # 그 범위들을 더해준다

    print(f'#{test_case} {count}')                              # 답을 프린트 한다.


