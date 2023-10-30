import sys

N = int(input())

arr = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)                    # 양방향으로 인접리스트를 만들어준다.
    arr[b].append(a)


answer = [0] * (N+1)                    # 답을 담아줄 공간

for _ in range(N+1):
    for i in range(N+1):
        if len(arr[i]) == 1:                # 만약 그 인접리스트(노드)에 들어있는 숫자가 한가지라면 맨 아래 자식노드이므로
            answer[i] = arr[i][0]           # 그 숫자가 바로 그 노드의 부모숫자이므로 답으로 담아준다.
            son = i                         # 자식 노드를 저장한다.
            for j in range(N+1):
                if son in arr[j]:        # 부모 노드가 다른 노드의 연결된 노드 리스트에 있다면
                    arr[j].remove(son)       # 해당 부모 노드를 제거


for i in range(2, len(answer)):
    print(answer[i])