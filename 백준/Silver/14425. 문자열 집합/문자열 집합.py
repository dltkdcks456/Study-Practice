N, M = map(int,input().split())
N_str = set(input() for i in range(N))
M_str = [input() for j in range(M)]
cnt = 0
for text in N_str:
    cnt += M_str.count(text)

print(cnt)