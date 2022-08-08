N = list(map(int, input().split()))

A = N[:2]
B = N[2:4]
C = N[4:6]

length = []
length_sum = []
ans = 0

if  A == B or A == C or B == C: # 같은 좌표가 있을 경우
    ans = -1
elif A[0] - B[0] == 0 or C[0] - B[0] == 0 or A[0] - C[0] == 0: # x의 값이 0
    if (A[0] - B[0] == 0 and C[0] - B[0] == 0) or (A[0] - B[0] == 0 and C[0] - A[0] == 0) or (C[0] - B[0] == 0 and C[0] - A[0] == 0):
        ans = -1
    else:
        length.append(((A[1] - B[1]) ** 2 + (A[0] - B[0]) ** 2 ) ** (1/2) )
        length.append(((C[1] - B[1]) ** 2 + (C[0] - B[0]) ** 2 ) ** (1/2) )
        length.append(((A[1] - C[1]) ** 2 + (A[0] - C[0]) ** 2 ) ** (1/2) )
elif (A[1] - B[1]) / (A[0] - B[0]) == (C[1] - B[1]) / (C[0] - B[0]): # 일직선 상에 존재
    ans = -1
else: # 각 변의 길이를 구해줌
    length.append(((A[1] - B[1]) ** 2 + (A[0] - B[0]) ** 2 ) ** (1/2) )
    length.append(((C[1] - B[1]) ** 2 + (C[0] - B[0]) ** 2 ) ** (1/2) )
    length.append(((A[1] - C[1]) ** 2 + (A[0] - C[0]) ** 2 ) ** (1/2) )

if ans == -1:
    print(-1)
else:
    for i in range(len(length) - 1):
        for j in range(i + 1, len(length)):
            length_sum.append(2 * (length[i] + length[j]))
    print(f'{max(length_sum) - min(length_sum):.15f}')