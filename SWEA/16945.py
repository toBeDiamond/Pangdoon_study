def f(i, N):
    if i == N:    # 순열 완성
        go.append(p[0:3])
        back.append(p[3:6])
        return
    else:   # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:     # 아직 사용되기 전이면
                p[i] = card[j]
                used[j] = 1
                f(i+1, N)
                used[j] = 0


T = int(input())
for test_case in range(1, T+1):
    card = list(map(int, input()))
    used = [0] * 6  # 이미 사용한 카드인지
    p = [0] * 6
    go = []
    back = []
    f(0, 6)
    # print(go)
    # print(back)
    flag = 0

    for i in range(len(go)//2):
        if (go[i][0] == go[i][1] == go[i][2] or go[i][0]+2 == go[i][1]+1 == go[i][2]) and (back[i][0] == back[i][1] == back[i][2] or back[i][0]+2 == back[i][1]+1 == back[i][2]):
            flag = 1

    print(f'#{test_case} {flag}')
