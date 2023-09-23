# T = int(input())
#
# for test_case in range(1, T+1):
#     N, P = map(int, input().split())
#
#     ans = N // P
#     ans1 = N % P
#     if N % P == 0:
#         ans2 = ans
#     else:
#         ans2 = ans + ans1
#
#     if N % P == 0:
#         result = ans ** P
#     else:
#         result = (ans ** (P - (N % P))) * ((ans + 1) ** (N % P))
#
#     print(f'#{test_case} {result}')

T = int(input())

for test_case in range(1, T+1):
    N, P = map(int, input().split())
    ans = N // P

    result = (ans ** (P - (N % P))) * ((ans + 1) ** (N % P))
    print(f'#{test_case} {result}')