# # nPn
# def perm(n, k): # n은 원소갯수, k: depth
#     if n == k:
#         print(p)
#         return
#     else:
#         for i in range(n):
#             if visited[i] == 0:
#                 visited[i] = 1
#                 p[k] = a[i]
#                 perm(n, k+1)
#                 visited[i] = 0
#
# a = [1, 2, 3]
# N = len(a)
# p = [0] * N
# visited = [0] * N
# perm(N, 0)

# T = int(input())
#
# for test_case in range(1, T+1):
#     N = int(input())
#     works = [list(map(int, input().split())) for _ in range(N)]
#     for work in range(N):1


# def perm(N, k, temp):
#     global max_v
#     # 가지치기
#     if temp <= max_v:
#         return
#     if N == k:
#         if max_v < temp:
#             max_v = temp
#         return
#     # 유도부분
#     else:
#         for i in range(k, N):
#             A[k], A[i] = A[i], A[k]
#             perm(N, k + 1, temp * 0.01 * arr[k][A[k]])
#             A[k], A[i] = A[i], A[k]
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     A = [i for i in range(N)]
#     max_v = 0
#     perm(N, 0, 1)
#     print(f'#{tc} {max_v * 100:.6f}')


def f(n, k, s):  # n: 원소의 개수, k: 재귀의 깊이, s: 총합
    global result

    if n == k:  # 순열 완성 => max_v에 저장 후 종료
        if result < s:
            result = s
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1  # 방문체크
                f(n, k + 1, s * (arr[k][i]) / 100)
                visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    result = 0
    f(N, 0, 1)
    print(f'#{tc} {result * 100:0.6f}')

