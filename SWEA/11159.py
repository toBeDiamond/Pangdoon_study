# T = int(input())
#
# for test_case in range(1, T + 1):
#     H, W = map(int, input().split())
#     count_list = [[0] * W for _ in range(H)]
#     cnt = 0
#     for i in range(H):
#         for j in range(W):
#             cnt += 1
#             count_list[i][j] = cnt
#
#     print(f'#{test_case}')
#     for i in range(H):
#         print(*count_list[i])
#
T = int(input())

for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    print(f'#{test_case}')
    cnt = 0
    for i in range(H):
        for j in range(W):
            cnt += 1
            print(cnt, end =' ')
        print()




