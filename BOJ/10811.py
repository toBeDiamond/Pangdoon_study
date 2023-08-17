N, M = map(int, input().split())
count = list(range(1, N+1))
for i in range(M):
    start, end = map(int, input().split())
    # count[start-1:end] = count[start-1:end][::-1]
    t = end - start + 1
    for j in range(t//2):
        count[start+j-1], count[end-j-1] = count[end-j-1], count[start+j-1]
print(*count)

