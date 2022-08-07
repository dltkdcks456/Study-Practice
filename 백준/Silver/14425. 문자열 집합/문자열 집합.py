import sys
N, M = map(int,sys.stdin.readline().split())
text_set = set(sys.stdin.readline() for i in range(N))
cnt = 0
for i in range(M):
    if sys.stdin.readline() in text_set:
        cnt += 1
print(cnt)