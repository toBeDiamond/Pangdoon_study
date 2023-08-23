T = int(input())

for test_case in range(1, T + 1):
    S = list(input())
    N = len(S)
    count = [[0] * 14 for _ in range(4)]

    for i in range(0, N, 3):  # S D H C 차례로
        num = ''
        for j in range(i + 1, i + 3):  # 01 02 03 04 숫자들만
            num += S[j]
        # 기호 , 카드값 알고있음
        # 조건문 기호 나눠주고 넣기전에 카드가 이미 들어있냐 ?
        num = int(num)
        if S[i] == 'S':
            count[0][num] += 1
        elif S[i] == 'D':
            count[1][num] += 1
        elif S[i] == 'H':
            count[2][num] += 1
        elif S[i] == 'C':
            count[3][num] += 1

    print(f'#{test_case}', end=' ')
    flag = 0
    res = []
    for i in range(4):
        total = 13
        for j in range(14):
            if count[i][j] >= 2:
                flag = 1
            else:
                total -= count[i][j]
        if not flag:
            res.append(total)
    if flag == 1:
        print("ERROR", end=' ')
    if flag == 0:
        print(*res, end=' ')
    print()