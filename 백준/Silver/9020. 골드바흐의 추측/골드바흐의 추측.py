def prime(n):
    num_list = [False] * 2 + [True] * (n - 1)
    
    for num in range(int(n ** 0.5 + 1)):
        if num_list[num]:
            for prod_num in range(num + num, n + 1, num):
                num_list[prod_num] = False
    
    return num_list

prime_list = prime(10000)

def partition(n):
    j = n // 2
    for i in range(j, 1, -1):
        if prime_list[i] and prime_list[n - i]:
            return i, n - i

T = int(input())
for i in range(T):
    n = int(input())
    a, b = partition(n)
    print(a, b)
