T = int(input())    # 테스트 케이스 개수를 input()

for test_case in range(1, T+1):             # 테스트 케이스 개수뽑아주기
    N = int(input())                        # 얼마 넣는지 N원 넣어주기.
    count = [0] * 8                     # 10원, 50원 ... 50,000원까지 8개의 빈 리스트
    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]             # 8개 종류의 돈들을 리스트로 가져오기(인덱스로 사용)

    for i in range(8):              # 8가지 종류를 돌아볼 것이기 때문에 8로 범위지정
        change = N // coin[i]       # 거스름돈은 N원 나누기 50000, 10000.... 50, 10 들
        count[i] += change          # 나눈 몫을 빈 배열에 넣어주기
        N = N % coin[i]             # 나누고 난다음 나머지 돈을 다시 for문으로 돌려야 하므로 N값을 바꿔준다.

    print(f'#{test_case}')
    print(*count)      # print를 해주는데 count 같은경우는 리스트로 되어있으므로 언패킹 시켜준다.
