
def dfs(v):
    visited[v] = 1
    for i in arr[v]:
        if visited[i]==0:
            dfs(i)


# def dfs(v):
#     visited[v] = 1
#     for i in range(C+1):
#         if arr[v][i] == 1 and visited[i]==0:
#             dfs(i)

C = int(input())
N = int(input())
visited = [0] * (C+1)
arr = [[] for _ in range(C+1)]
for i in range(N):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

# arr = [[0] * (C+1) for _ in range(C+1)]
# visited = [0] * (C+1)
# for i in range(N):
#     a, b = map(int, input().split())
#     arr[a][b] = 1
#     arr[b][a] = 1


dfs(1)
print(sum(visited)-1)




