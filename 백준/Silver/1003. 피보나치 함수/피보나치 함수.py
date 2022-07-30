T = int(input())

for i in range(T):
    n = int(input())
    fibo_memo = {0: 0, 1: 1}
    cnt0_memo = {0: 1, 1: 0}
    cnt1_memo = {0: 0, 1: 1}
    def fibo(n):
        if n == 0:
            return n
        elif n == 1:
            return n
        elif n in fibo_memo:
            n = fibo_memo[n]
            return n
        else:
            fibo_memo[n] = fibo(n - 1) + fibo(n - 2)
            cnt0_memo[n] = cnt0_memo[n - 1] + cnt0_memo[n - 2]
            cnt1_memo[n] = cnt1_memo[n - 1] + cnt1_memo[n - 2]
            return fibo_memo[n]
    fibo(n)
    print(cnt0_memo[n], cnt1_memo[n])