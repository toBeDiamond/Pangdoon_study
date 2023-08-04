# for i in range(5):
#     for j in range(5):
#         print(f'{i}{j}', end=' ')
#     print()

    #     if i == j:
    #         print('#', end='')
    #     else:
    #         print('+', end='')
    # print()  # 줄 바꿈

for i in range(5):
    lst = ['+']*5
    lst[i] = '#'
    print(''.join(lst))