T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    minV = 1
    for i in range(2, a + 1):
        while a % i == 0 and b % i == 0:
            a = a // i
            b = b // i
            minV *= i
    print(minV * a * b)