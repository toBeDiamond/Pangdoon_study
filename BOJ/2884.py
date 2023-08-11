H, M = map(int,input().split())

if M > 44 and H >= 0:
    print(H, M - 45)
if M < 45 and H > 0:
    print(H - 1, M + 15)
if: M < 45 and H == 0:
    print(23, M + 15)