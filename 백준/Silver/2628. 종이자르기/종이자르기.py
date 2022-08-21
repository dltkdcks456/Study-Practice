C, R = map(int, input().split())
T = int(input())
r_0 = []
c_1 = []
for _ in range(T):
    a, b = map(int, input().split())
    if a == 0:
        r_0.append(b)
    else:
        c_1.append(b)
r_0 = [0] + r_0 + [R]
c_1 = [0] + c_1 + [C]
r_0.sort()
c_1.sort()

maxV = 0
for i in range(1, len(r_0)):
    for j in range(1, len(c_1)):
        area = (r_0[i] - r_0[i - 1]) * (c_1[j] - c_1[j - 1])
        if area > maxV:
            maxV = area
print(maxV)