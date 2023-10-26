import sys

N, D = map(int, input().split())
edges = []
for _ in range(N):
    S, G, L = map(int, input().split())
    edges.append((S, G, L))

edges.sort(key=lambda x: x[1])  # G를 기준으로 정렬

dp = [float('inf')] * (D + 1)
dp[0] = 0

for i in range(1, D + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)  # 이전 위치에서 1만큼 진행
    for S, G, L in edges:
        if i == G:
            dp[i] = min(dp[i], dp[S] + L)  # 경로를 따라 이동

print(dp[D])