T = int(input())
for test_case in range(1, T+1):
    G = int(input())  # 나사의 개수
    L = list(map(int, input().split()))  # 나사 리스트 (앞,뒤)
    nasa = []
    solo = 0
    S = len(nasa)
    for i in range(1, len(L), 2):
        if L.count(L[i]) == 1:
            solo = L[i]

    for i in range(0, len(L), 2):
        nasa.append([L[i], L[i+1]])

    for i in range(len(nasa)):
        if i != len(nasa)-1:
            if nasa[i][1] == solo:
                nasa[i], nasa[i+1] = nasa[i+1], nasa[i]

    for i in range(len(nasa)-1, 0, -1):
        for j in range(i):
            if nasa[i][0] == nasa[j][1]:
                nasa[i-1], nasa[j] = nasa[j], nasa[i-1]

    ans = ""
    for i in range(len(nasa)):
        for j in range(2):
            ans += str(nasa[i][j])
            ans += " "

    print(f'#{test_case} {ans}')


