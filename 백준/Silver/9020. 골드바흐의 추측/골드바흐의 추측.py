import sys

def prime(n):
    num_list = [True] * (n + 1)
    prime_num_list = []
    
    for num in range(int(n ** 0.5 + 1)):
        if num == 0 or num == 1:
            num_list[num] = False
        else:
            for prod_num in range(num + num, n + 1, num):
                num_list[prod_num] = False
    
    for prime, bool_ in enumerate(num_list):
        if bool_ == True:
            prime_num_list.append(prime)
    return prime_num_list

prime_list = prime(10000)
T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    half_prime_list = sorted([i for i in prime_list if i <= n//2], reverse = True)
    a = True
    for x in half_prime_list:
        if a == False:
            break
        for y in prime_list:
            if x + y == n:
                print(x, y)
                a = False
                break
