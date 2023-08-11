X = int(input())
N = int(input())

total = 0
for i in range(N):
    a, b = map(int, input().split())
    price = a * b
    total += price

if total == X:
    print("Yes")
else:
    print("No")
