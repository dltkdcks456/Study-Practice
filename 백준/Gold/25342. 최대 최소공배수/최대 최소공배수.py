import sys
input = sys.stdin.readline

def gcb(a, b):
    if b == 0:
        return a
    return gcb(b, a % b)

def LCM(li):
    temp = gcb(li[0], li[1])
    lcm = li[0] * li[1] // temp
    temp = gcb(lcm, li[2])
    lcm = lcm * li[2] // temp
    return lcm


T = int(input())
for _ in range(T):
    N = int(input())
    if N == 3:
        print(6)
    elif N == 4:
        print(12)
    else:
        if N % 2:           #홀수 일 때
            li = [[N - 1, N - 2, N], [N, N - 2,N - 3]]
            maxV = 0
            for i in li:
                temp = LCM(i)
                if temp > maxV:
                    maxV = temp
            print(maxV)
        else:               #짝수 일 때
            li = [[N - 4, N - 3, N - 1], [N - 1, N - 2, N - 3], [N - 3, N - 1, N]]
            for j in li:
                temp = LCM(j)
                if temp > maxV:
                    maxV = temp
            print(maxV)