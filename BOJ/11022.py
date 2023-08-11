T = int(input())

for test_case in range(1, 1 + T):
    A, B = map(int, input().split())
    ans = A + B

    print(f'Case #{test_case}: {A} + {B} = {ans}')