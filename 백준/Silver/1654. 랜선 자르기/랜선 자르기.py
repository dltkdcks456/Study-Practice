K, N = map(int, input().split())
li = sorted([int(input()) for _ in range(K)])
start = 1
end = li[-1]

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in li:
        cnt += i // mid
    if cnt < N:
        end = mid - 1
    elif cnt >= N:
        start = mid + 1
print(end)