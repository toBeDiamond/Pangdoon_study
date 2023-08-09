A, B = map(int, input().split())
C = int(input())

if B + C < 60 and A <= 23:
    print(A, B+C)

elif B + C >= 60 and A + (B+C)//60 >= 24:
    print((A + ((B+C)//60) - 24), (B + C) % 60)

elif B + C >= 60 and A + ((B+C)//60) < 24:
    print(A + ((B + C) // 60), (B + C) % 60)

elif B + C < 60 and A + ((B+C)//60) < 24:
    print(A + ((B + C) // 60), (B + C) % 60)


