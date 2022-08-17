import sys

N, K = map(int, sys.stdin.readline().split())
room = {}
for i in range(N):
    student = sys.stdin.readline()
    if student in room:
        room[student] += 1
    else:
        room[student] = 1
cnt = 0
for j in room.values():
    if j % K:
        cnt += j//K + 1
    else:
        cnt += j//K
print(cnt)