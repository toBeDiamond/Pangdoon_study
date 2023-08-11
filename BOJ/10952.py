while 1:
    A, B = map(int, input().split())
    ans = A + B
    if A + B == 0:
        break
    else:
        print(A + B)