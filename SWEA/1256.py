T = int(input())

for test_case in range(1, T + 1):
    K = int(input())
    word = input()

    word_ans = []
    for i in range(len(word)):
        word_ans.append(word[i:])

    word_ans.sort()

    print(f'#{test_case}', end=' ')
    if word_ans[K-1]:
        print(f'{word_ans[K-1]}', end=' ')
    else:
        print('none', end=' ')
    print()