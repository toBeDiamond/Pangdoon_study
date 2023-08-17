# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     counts = [[0] * N for _ in range(N)]
#     di = (-1, -1)
#     dj = (-1, 0)
#     for i in range(N):
#         counts[i][0] = 1
#         for j in range(N):
#             for k in range(2):
#                 if 0 <= i+di[k] < N and 0 <= j+dj[k]:
#                     counts[i][j] = i+di[k] + j+dj[k]
#     print(f'#{test_case}')
#     for i in counts:
#         print(i)

# --------------------------------------------------------------------------------------------

# T = int(input())
#
# for test_case in range(1, T + 1):
#     N = int(input())
#     counts = [[0] * N for _ in range(N)]
#     di = (-1, -1)  # 델타 값 설정
#     dj = (-1, 0)
#
#     for i in range(N):
#         counts[i][0] = 1
#         for j in range(1, N):
#             for k in range(2):
#                 prev_i = i + di[k]
#                 prev_j = j + dj[k]
#                 if 0 <= prev_i < N and 0 <= prev_j < N:  # 유효한 범위 내에서만 더하기
#                     counts[i][j] += counts[prev_i][prev_j]
#
#     print(f'#{test_case}')
#     for i in counts:
#         print(' '.join(map(str, i)))

# --------------------------------------------------------------------------
T = int(input())

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    counts = [[0] * N for _ in range(N)]  # 삼각형을 채울 빈 배열
    counts[0][0] = 1  # 초기값. 점화식의 맨 앞에 있음.
    di = (-1, -1)  # 전 숫자들을 보겠다
    dj = (-1, 0)   # 전 숫자들의 왼쪽과 위를 보겠다.
    for i in range(1, N):  # 맨 위는 1로 채웠으니 그 아래부터 1, 1 / 1, 2, 1... 처럼 채워나가겠다
        for j in range(i+1):  # 대각선까지만 진행하면 되니까 i+1까지
            for k in range(2):  # 두 개를 모두 보는데
                ni = i+di[k]    # 위
                nj = j+dj[k]    # 왼쪽, 위
                if 0 <= ni:     # 맨 왼쪽은 -1 이 인덱스에 없으니까 제외하고
                    counts[i][j] += counts[ni][nj]
    print(f'#{test_case}')
    for i in range(N):
        for j in range(i+1):  # 대각선 긋고 거기까지만 0부터 i까지 출력하겠다
            print(counts[i][j], end=' ')  # 구분자는 공백문자 ' ' 이다
        print()  # 한 줄 띄우고



