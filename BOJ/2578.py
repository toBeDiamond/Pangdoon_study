def findRow(i, j):
    global result
    count = 0
    for k in range(5):
        if arr[k][j] == 0:
            count += 1
    if count == 5:
        result += 1


def findCol(i, j):
    global result
    count = 0
    for k in range(5):
        if arr[i][k] == 0:
            count += 1
    if count == 5:
        result += 1


def findRU(i, j):
    global result
    count = 0
    for k in range(5):
        if arr[k][k] == 0:
            count += 1
    if count == 5:
        result += 1

def findLU(i, j):
    global result
    count = 0
    for k in range(5):
        if arr[k][4-k] == 0:
            count += 1
    if count == 5:
        result += 1

arr = [list(map(int, input().split())) for _ in range(5)]
result = 0     # 빙고가 3개면 끝

call = []      # 사회자가 부르는 숫자들
for _ in range(5):
    a, b, c, d, e = map(int, input().split())
    call.append(a)
    call.append(b)
    call.append(c)
    call.append(d)
    call.append(e)


calling_count = 0
for k in call:
    calling_count += 1

    for i in range(5):
        for j in range(5):
            if arr[i][j] == k:
                arr[i][j] = 0
                findRow(i, j)
                findCol(i, j)
                if i == j:
                    findRU(i, j)
                if i + j == 4:
                    findLU(i, j)
                if result >= 3:
                    print(calling_count)
                    break
        if result >= 3:
            break
    if result >= 3:
        break






