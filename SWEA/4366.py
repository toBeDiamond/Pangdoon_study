T = int(input())
for test_case in range(1, T + 1):
    binary = list(map(int, input()))
    trinary = list(map(int, input()))
    N2 = len(binary)
    N3 = len(trinary)
    N2_list = []
    N3_list = []
    for i in range(N2):
        if binary[i] == 0:
            binary[i] = 1
            N2_list.append(binary[0:])
            binary[i] = 0
        elif binary[i] == 1:
            binary[i] = 0
            N2_list.append(binary[0:])
            binary[i] = 1

    for i in range(N3):
        if trinary[i] == 1:
            trinary[i] = 0
            N3_list.append(trinary[0:])
            trinary[i] = 2
            N3_list.append(trinary[0:])
            trinary[i] = 1
        if trinary[i] == 0:
            trinary[i] = 1
            N3_list.append(trinary[0:])
            trinary[i] = 2
            N3_list.append(trinary[0:])
            trinary[i] = 0
        if trinary[i] == 2:
            trinary[i] = 0
            N3_list.append(trinary[0:])
            trinary[i] = 1
            N3_list.append(trinary[0:])
            trinary[i] = 2

    ans = []
    for i in N2_list:
        binary_str = ""
        for j in i:
            binary_str += str(j)
        ans.append(binary_str)

    result = []
    for i in N3_list:
        binary_str = ""
        for j in i:
            binary_str += str(j)
        result.append(binary_str)

    N2_real_list = []
    for i in range(len(ans)):
        N2_real_list.append(int(ans[i], 2))
    N3_real_list = []
    for i in range(len(result)):
        N3_real_list.append(int(result[i], 3))

    total = 0
    for i in range(len(N2_real_list)):
        if N2_real_list[i] in N3_real_list:
            total = N2_real_list[i]
            break

    print(f'#{test_case} {total}')

