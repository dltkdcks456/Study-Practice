import sys

def calculation(n, m, sumV):
    global maxV, minV
    if n == m - 1:
        maxV = max(maxV, sumV)
        minV = min(minV, sumV)
        return
    else:
        for i in range(4):
            if cal[i] > 0:
                cal[i] -= 1
                if i == 0:
                    temp = sumV + num[n + 1]
                elif i == 1:
                    temp = sumV - num[n + 1]
                elif i == 2:
                    temp = sumV * num[n + 1]
                else:
                    temp = int(sumV / num[n + 1])
                calculation(n + 1, m, temp)
                cal[i] += 1


N = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))
maxV = -float('inf')
minV = float('inf')
calculation(0, N, num[0])
print(maxV)
print(minV)
