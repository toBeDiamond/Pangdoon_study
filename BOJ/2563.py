N = int(input())

count = [[0]*100 for _ in range(100)]
for _ in range(N):
    ar, br = map(int, input().split()) # 왼쪽 아래 모서리 시작점
    for i in range(ar, ar + 10):
        for j in range(br, br + 10):
            count[i][j] = 1

total = 0
for i in range(100):  # 10 > 100
    for j in range(100): # 10 > 100
        total += count[i][j]

print(total)