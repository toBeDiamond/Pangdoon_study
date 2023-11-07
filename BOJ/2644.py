N = int(input())
a, b = map(int, input().split())
m = int(input())

arr = [[] for _ in range(N+1)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

result = -1  # 시작 시 result를 -1로 설정
visited = [0] * (N+1)
count = 0  # count 변수를 함수 밖으로 뺍니다.

def dfs(k):
    global result
    global count
    visited[k] = 1

    if k == b:
        result = count
        return

    for i in arr[k]:
        if visited[i] == 0:
            count += 1
            dfs(i)
            count -= 1  # 이전 노드로 돌아갈 때 count를 감소시킵니다.

dfs(a)

print(result)