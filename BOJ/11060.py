import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
board = list(map(int, input().split()))

curr_idx, jump = 0, 0
queue = deque()
queue.append((curr_idx, jump))
visited = []

while queue:g
    curr_idx, jump = queue.popleft()
    if curr_idx == len(board) - 1:
        print(jump)
        exit()

    for i in range(1, board[curr_idx] + 1):
        next_idx = curr_idx + i
        if next_idx not in visited:
            queue.append((next_idx, jump + 1))
            visited.append(next_idx)
print(-1)