T = int(input())

for test_case in range(1, T+1):
    txt = input()
    stack = []

    for i in range(len(txt)):
        if txt[i] == "(" or txt[i] == "{":
            stack.append(txt[i])

        if txt[i] == ")" or txt[i] == "}":
            if stack and ((txt[i] == ")" and stack[-1] == "(") or (txt[i] == "}" and stack[-1] == "{")):
                stack.pop()
            else:
                stack.append(txt[i])

    if not stack:
        ans = 1
    else:
        ans = 0

    print(f'#{test_case} {ans}')