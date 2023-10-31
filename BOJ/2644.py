import sys
sys.setrecursionlimit(10**6)


N = int(input())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

arr = [[] for _ in range(N+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

result = 987654321
visited = [0] * (N+1)
count = 0
print(arr)
def dfs(k):
    global result
    global count
    visited[k] = 1
    if k == b:
        if result > count:
            result = count
            return

    for i in arr[k]:
        if visited[i] == 0:
            visited[i] = 1
            count += 1
            dfs(i)
            count -= 1



dfs(a)
if result == 987654321:
    print('-1')
else:
    print(result)

