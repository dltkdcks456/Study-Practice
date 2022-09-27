import sys

N = int(input())
dp1 = [0] + [1] * 9
dp2 = [0] * 10
ch = 1

while ch < N:
    if ch % 2:
        for i in range(10):
            r_i = i + 1
            l_i = i - 1
            if 0 <= l_i < 10 and 0 <= r_i < 10:
                dp2[i] = dp1[l_i] + dp1[r_i]
            elif 0 <= l_i < 10:
                dp2[i] = dp1[l_i]
            elif 0 <= r_i < 10:
                dp2[i] = dp1[r_i]
    else:
        for i in range(10):
            r_i = i + 1
            l_i = i - 1
            if 0 <= l_i < 10 and 0 <= r_i < 10:
                dp1[i] = dp2[l_i] + dp2[r_i]
            elif 0 <= l_i < 10:
                dp1[i] = dp2[l_i]
            elif 0 <= r_i < 10:
                dp1[i] = dp2[r_i]
    ch += 1
if ch % 2:
    print(sum(dp1)%1000000000)
else:
    print(sum(dp2)%1000000000)