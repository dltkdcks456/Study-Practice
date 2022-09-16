import sys
input = sys.stdin.readline
N, M = map(int, input().split())
li = list(map(int, input().split()))
end = max(li)
start = 1
while start <= end:
    rest = 0
    mid = (start + end) // 2
    for i in li:
        if i > mid:
            rest += i - mid
    if rest > M:
        start = mid + 1
    elif rest < M:
        end = mid - 1
    else:
        print(mid)
        break
else:
    print(end)