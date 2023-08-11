T = int(input())

if T % 4 == 0 and T % 100 != 0 or T % 400 == 0:
    ans = 1
else:
    ans = 0

print(ans)