import sys

N, M, B = map(int, sys.stdin.readline().split())
block = []
for _ in range(N):
    block.extend(map(int, sys.stdin.readline().split()))

minV = min(block)
maxV = max(block)

ans_time = 0
ans_height = 0

for i in range(minV, maxV + 1):
    height = block[:]
    sum_minus = sum_plus = time = 0

    for j in range(N * M):
        height[j] -= i
        if height[j] < 0:
            sum_minus += height[j]
        else:
            sum_plus += height[j]

    if sum_minus + sum_plus + B < 0:
        continue
    else:
        if sum_minus <= B:
            time += abs(sum_minus) + 2 * (sum_plus)
        else:
            rest = sum_minus + B
            fill = sum_plus + rest
            time += abs(sum_minus) + 3 * rest + 2 * fill

    if ans_time == 0:
        ans_time = time
        ans_height = i
    else:
        if time <= ans_time:
            ans_time = time
            ans_height = i

print(ans_time, ans_height)