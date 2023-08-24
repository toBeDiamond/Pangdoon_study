T = int(input())            # 테스트 케이스 수 받기
for test_case in range(1, T+1):                 # 테스트 케이스 수 돌리기
    arr = list(map(int, input()))               # 0011 을 리스트 값으로 받기 [0,0,1,1]
    N = len(arr)                                # 리스트 개수를 N으로 두기
    count = [0] * N                             # N개의 0으로 구성된 리스트 만들기 [0, 0, 0, 0]

    ans = 0             # 답으로 나올 변수 지정하기
    for i in range(N):              # 리스트의 개수만큼 for문 돌리기
        if arr[i] != count[i]:              # arr 리스트의 인덱스 값들이 0이 아니라면, 차례로 [0, 0, 1, 1] 이 [0, 0, 0, 0] 아니라면
            ans += 1                        # 바꿔줘야 하므로, 1을 올린다.
            for j in range(i, N):           # for문을 통해서 그 뒷 부분을 다 바꿔준다.
                count[j] = arr[i]           # 0 0 0 0 > 0 0 1 1 = 1번
                                            # 0 0 0 > 1 1 1 > 1 0 0 = 2번
    print(f'#{test_case} {ans}')