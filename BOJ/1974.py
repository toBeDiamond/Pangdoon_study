import sys
sys.stdin=open('1974.txt')

T = int(input())

for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    ans = True

    for i in range(9):   # row 우선
        s1 = set()
        for j in range(9):
            s1.add(arr[i][j])
        if len(s1) != 9:
            ans = False

    for j in range(9):    # col 우선
        s2 = set()
        for i in range(9):
            s2.add(arr[i][j])
        if len(s2) != 9:
            ans = False


    for i in range(3):    # 3X3 찾기
        for j in range(3): # set
            s3 = set()
            for m in range(3):
                for k in range(3):
                    s3.add(arr[m+3*i][k+3*j])
            if len(s3) != 9: # 들여쓰기 주의
                ans = False

    if ans == True:
        real_ans = 1
    else:
        real_ans = 0

    print(f'#{test_case} {real_ans}')