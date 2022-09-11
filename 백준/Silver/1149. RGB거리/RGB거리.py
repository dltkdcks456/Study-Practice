N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))
    
for i in range(1, N):
    li[i][0] = min(li[i - 1][1], li[i - 1][2]) + li[i][0]
    li[i][1] = min(li[i - 1][0], li[i - 1][2]) + li[i][1]
    li[i][2] = min(li[i - 1][0], li[i - 1][1]) + li[i][2]
    
print(min(li[N - 1]))