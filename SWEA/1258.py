T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    count_box_x = []
    for i in range(N):
        count_x = 0
        for j in range(N):
            if arr[i][j] != 0:
                count_x += 1
                if j < N-1:
                    if arr[i][j+1] == 0:
                        count_box_x.append(count_x)
            if arr[i][j] == 0:
                count_x = 0

        else:
            count_box_x.append(count_x)

    x_box = []
    for i in count_box_x:
        if i != 0:
            x_box.append(i)

    x_box.sort()

    cnt_box = [0] * (N+1)
    for i in range(len(x_box)):
        cnt_box[x_box[i]] += 1

    Y_box = []
    for i in cnt_box:
        if i != 0:
            Y_box.append(i)

    X_box = sorted(list(set(x_box)))

    ans = []
    for i in range(len(X_box)):
        ans.append([Y_box[i], X_box[i]])

    ans.sort(key=lambda x: (x[0] * x[1], x[0]))
    count = len(X_box)
    print(f'#{test_case} {count}',end = ' ')

    for i in range(len(ans)):
        print(*ans[i],end=' ')

    print()


