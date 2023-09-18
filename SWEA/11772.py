def binarySearch(arr, target):
    global count
    
    low = 0
    high = len(arr) - 1
    flag = 0
    #low > high 라면 데이터를 못찾은 경우
    while low <= high:
        mid = (low + high) // 2
         
        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            count += 1
            return
        
        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid + 1
            if flag == -1:
                return
            else:
                flag = -1

        
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid - 1
            if flag == 1:
                return
            else:
                flag = 1
    
    return "해당 데이터는 없습니다"

T = int(input())                 # 테스트 케이스 개수

for test_case in range(1, T+1):
    N, M = map(int, input().split())  # N,M 의 개수
    A = sorted(map(int, input().split()))  # A의 리스트
    B = list(map(int, input().split()))  # B의 리스트
    count = 0
    for b in B:
        binarySearch(A, b)

    print(f'#{test_case} {count}')



