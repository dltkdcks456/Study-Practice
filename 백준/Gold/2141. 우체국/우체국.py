import sys
input = sys.stdin.readline

N = int(input())
li = []
right_people = 0
for _ in range(N):
    a, b = map(int, input().split())
    right_people += b
    li.append([a, b])
li.sort()
right_people -= li[0][1]
minV = float('inf')
pos = left_people = 0
for i in range(N):
    if i >= 1:
        left_people += li[i - 1][1]
        right_people -= li[i][1]
    diff = abs(left_people - right_people)
    if diff < minV:
        minV = diff
        pos = li[i][0]
print(pos)