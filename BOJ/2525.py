A, B = map(int, input().split())
C = int(input())

if B + C > 60:
    print(A + C // 60 , B + C - 60)
elif B + C < 60:
    print(C, B + C)
elif A == 23 and B + C > 60:
    print(0, B + C - 60)
