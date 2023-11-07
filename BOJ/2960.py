from collections import deque

N, K = map(int, input().split())

Q = deque()
count = 0
for i in range(2, N+1):
    Q.append(i)
count = 0
while Q:
    tmp = Q.popleft()
    count += 1
    if count == K:
        print(tmp)
        break
    for _ in range(len(Q)):
        temp = Q.popleft()
        if temp % tmp == 0:
            count += 1
            if count == K:
                print(temp)
                break
        else:
            Q.append(temp)




