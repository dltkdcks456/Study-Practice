def fac(a):
    if a <= 1:
        return 1
    else:
        return a * fac(a - 1)
n, m = map(int, input().split())
print(fac(n)//fac(n - m)//fac(m))