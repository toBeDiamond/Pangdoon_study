def binarySearch(low, high, target):
    # 기저 조건 : 언제까지 재귀호출을 반복할 것인가?
    # low > high 라면 데이터를 못찾음
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # 1. 가운데 값이 정답인 경우
    if target == arr[mid]:
        return mid
        
    # 2. 가운데 값이 정답보다 작은 경우
    if target > arr[mid]:
        return binarySearch (mid + 1, high, target)
        
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch (low, mid - 1, target)
    

        