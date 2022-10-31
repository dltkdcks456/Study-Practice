import sys

N, M, Q = map(int, sys.stdin.readline().split())
data = []
for _ in range(M):
    data.append(list(map(int, sys.stdin.readline().split())))

*R_W, R_B = list(map(int, sys.stdin.readline().split()))

dict1 = {i:0 for i in range(1, N + 1)}
total_sum = R_B
for i in range(M):
    total_sum += R_W[i] * data[i][-1]
    for k in range(data[i][0]):
        dict1[data[i][1 + k]] += data[i][1 + k + data[i][0]] * R_W[i]

for _ in range(Q):
    temp = total_sum
    A = [0] + list(map(int, sys.stdin.readline().split()))
    for j in range(1, N + 1):
        temp += dict1[j] * A[j]
    print(temp)