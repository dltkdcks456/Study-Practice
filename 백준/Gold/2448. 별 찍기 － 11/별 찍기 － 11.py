import sys

def triangle(N):
    if N == 3:
        return ['  *  ', ' * * ', '*****']
    else:
        material = triangle(N // 2)
        new_triangle = []
        for i in range(2):
            if i == 0:
                for j in material:
                    temp = (' ' * (N // 2)) + j + (' ' * (N // 2))
                    new_triangle.append(temp)
            else:
                for k in material:
                    new_triangle.append(k + ' ' + k)
        return new_triangle


N = int(input())
ans = triangle(N)
for i in ans:
    print(i)