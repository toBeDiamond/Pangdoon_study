T = int(input())                                # 테스트 케이스 개수 받기
for testcase in range(1, T+1):                  # 테스트 케이스 개수 만큼 돌려주기
    N = int(input())                            # 카드 개수
    arr = list(map(str, input().split()))       # 카드 받기
    total = [0] * N                             # 0으로 채워진 빈 리스트 만들기 (인덱스를 사용할 것이기 때문)

    if N % 2 == 0:                              # 짝수라면
        for i in range(N//2):                   # 반틈만 돌려준다 ( 반틈 나누었을 때 앞부분 )
            total[i*2] = arr[i]                 # 앞부분 반틈을 0 2 4 ... 인덱스로 넣어준다
        for j in range(N//2, N):                # 반틈 나눈 것부터 마지막 까지 (뒷부분)
            total[(j-(N//2))*2+1] = arr[j]      # 뒷부분 반틈을 1, 3, 5 인덱스로 넣어준다

    if N % 2 == 1:                              # 홀수라면
        for i in range((N+1)//2):               # 반틈을 돌려준다 그런데 홀수는 딱 반틈이 생기지 않으므로 앞부분에 1개를 더 넣는다.
            total[i*2] = arr[i]                 # 앞부분 반틈을 0 2 4 ... 인덱스로 넣어준다
        for j in range(N//2+1, N):              # 반틈 나눈 것부터 마지막 까지 (뒷부분)
            total[(j-(N//2+1))*2+1] = arr[j]    # 뒷부분 반틈을 1, 3, 5 인덱스로 넣어준다

    print(f'#{testcase}', *total)               # 언패킹을 해서 꺼내준다

