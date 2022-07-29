N, M = map(int, input().split())

number_list = [True] * (M + 1)

for i in range(int(M ** 0.5 + 1)):
    if i == 0 or i == 1:
        number_list[i] = False
    else:
        for j in range(i + i, M + 1, i):
            number_list[j] = False

prime_number = [idx for idx in range(len(number_list)) if number_list[idx] == True]
for prime in prime_number:
    if N <= prime <= M:
        print(prime)