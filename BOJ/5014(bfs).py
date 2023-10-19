from collections import deque

def bfs(s, e):
    q = deque()
    v = [0] * (F+1)

    q.append(S)
    v[s] = 1

    while q:
        c = q.popleft()
        if c==e:
            return v[c]-1
        for n in (c+U, c-D):
            if 1<=n<=F and v[n]==0:
                q.append(n)
                v[n] = v[c] + 1
    return 'use the stairs'

F, S, G, U, D = map(int, input().split())

ans = bfs(S, G)
print(ans)