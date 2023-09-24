# def sosu_find(sosu):
#     global flag
#
#     for i in sosu_list:
#         if sosu % i == 0:
#             flag = 1
#             return
#     else:
#         sosu_list.append(sosu)
#         return sosu
#
# M, N = list(map(int, input().split()))
# sosu_list = [2, 3, 5, 7]
# su = [1, 2, 3, 5, 7]
# flag = 0
#
# for i in range(M, N+1):
#     if i in su:
#         print(i)
#     else:
#         sosu_find(i)
#         if flag == 1:
#             flag = 0
#             continue
#         else:
#             print(i)

# def is_prime(num):
#     if num < 2:
#         return False
#
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#
#     return True
#
# M, N = map(int, input().split())
#
# for num in range(M, N+1):
#     if is_prime(num):
#         print(num)


## 💬 **Code3  `성공` - 풀이 참고**

M, N = map(int, input().split())
a = [False, False] + [True] * (N - 1)
primes = []

for i in range(2, N+1):
    if a[i]:
        for j in range(2 * i, N + 1, i):
            a[j] = False
        if i >= M:
            primes.append(i)

for k in range(len(primes)):
    print(primes[k])


