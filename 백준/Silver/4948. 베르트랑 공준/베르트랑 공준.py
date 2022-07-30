def prime(n):
    max_num = 2 * n
    num_list = [True] * (max_num + 1)
    prime_number_list = []

    for i in range(int(max_num ** 0.5 + 1)):
        if i == 0 or i == 1:
            num_list[i] = False
        else:
            for j in range(i + i, max_num + 1, i):
                num_list[j] = False

    for idx, num in enumerate(num_list):
        if n < idx <= max_num and num == True:
            prime_number_list.append(idx)

    print(len(prime_number_list))

while True:
    n = int(input())
    if n != 0:
        prime(n)
    else:
        break