N, M = map(int,input().split())
text_set = set(input() for i in range(N))
cnt = 0
for i in range(M):
    if input() in text_set:
        cnt += 1
print(cnt)