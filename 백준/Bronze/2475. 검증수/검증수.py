li = list(map(int, input().split()))
sumV = 0
for i in li:
    sumV += i ** 2
print(sumV % 10)