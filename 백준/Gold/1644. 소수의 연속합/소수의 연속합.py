import sys
input = sys.stdin.readline


N = int(input())            # N = 1인 코너 케이스도 확인!!!
num = [1] * (N + 1)
num[0], num[1] = 0, 0
prime = []
for i in range(2, int(N ** 0.5) + 1):
    if num[i] == 1:
        for j in range(2 * i, N + 1, i):
            num[j] = 0

for k in range(2, N + 1):
    if num[k] == 1:
        prime.append(k)

point1 = point2 = -1
sumV = ans = 0
L = len(prime)

while True:
    if point2 == L - 1 and sumV <= N:
        break
    point2 += 1
    sumV += prime[point2]
    if sumV == N:
        ans += 1
    elif sumV > N:
        while sumV > N:
            point1 += 1
            sumV -= prime[point1]
        else:
            if sumV == N:
                ans += 1
print(ans)