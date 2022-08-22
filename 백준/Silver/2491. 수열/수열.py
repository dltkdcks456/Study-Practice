N = int(input())
li = list(map(int, input().split()))

T = len(li)
maxV = upper = lower = 1

for i in range(T - 1):
    if li[i + 1] >= li[i]:
        upper += 1
        if upper > maxV:
            maxV = upper
    else:
        upper = 1
    if li[i + 1] <= li[i]:
        lower += 1
        if lower > maxV:
            maxV = lower
    else:
        lower = 1
print(maxV)