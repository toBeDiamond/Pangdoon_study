x = int(input())
y = int(input())

if x > 0 and y > 0:
    ans = 1
elif x < 0 and y < 0:
    ans = 3
elif x < 0 and y > 0:
    ans = 2
else:
    ans = 4

print(ans)