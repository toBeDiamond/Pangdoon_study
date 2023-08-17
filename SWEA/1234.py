import sys
sys.stdin=open('1234.txt','r')

def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else :
        top -= 1
        return stack[top+1]

def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item


for test_case in range(10):
    size = 100
    stack = [0] * size
    top = -1
    A, B = map(str, input().split())
    A = int(A)
    B = list(B)
    for i in range(A):
        if B[i] == stack[top]:
            pop()

        elif B[i] != stack[top]:
            push(B[i], 100)

    ans = stack[0]
    for i in range(1, top + 1):
        ans += stack[i]
    print(f'#{test_case + 1} {ans}')



