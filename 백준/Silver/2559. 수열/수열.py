N, K = map(int, input().split())
num_li = list(map(int, input().split()))

maxV = start = sum(num_li[:K])

for i in range(1, N - K + 1):
    start = start - num_li[i - 1] + num_li[i + K - 1]
    if start > maxV:
        maxV = start
print(maxV)