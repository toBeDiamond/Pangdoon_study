T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())        # N = 개수, M은 이동 횟수
    Q = list(map(int, input().split()))
 
    for i in range(M):
        tmp = Q.pop(0)     # Q.append(Q.pop(0))
        Q.append(tmp)
 
    print(f'#{test_case} {Q[0]}')

#     T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())        # N = 개수, M은 이동 횟수
#     arr = list(map(int, input().split())) * 50
#     Q = []
 
#     for i in range(M+1):
#         Q.append(arr[i])
 
#     print(f'#{test_case} {Q[-1]}')