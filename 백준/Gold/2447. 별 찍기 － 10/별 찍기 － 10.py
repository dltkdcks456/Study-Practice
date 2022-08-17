def star(n):
    if n == 1:
        return ['*']
    else:
        stars = star(n // 3)
        L = []
        
        for S in stars:
            L.append(S * 3)
        for S in stars:
            L.append(S + ' ' * (n // 3) + S)
        for S in stars:
            L.append(S * 3)
        return L
N = int(input())
print('\n'.join(star(N)))