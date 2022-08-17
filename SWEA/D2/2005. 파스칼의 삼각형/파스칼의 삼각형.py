from collections import deque

T = int(input())
for test in range(T):
    pascal = deque([1])
    N = int(input())
    n = 1
    print(f'#{test + 1}', pascal[0], sep = '\n')
    while n < N:
        n += 1
        for i in range(len(pascal) - 1, 0, -1):
            pascal[i] = pascal[i] + pascal[i - 1]
        pascal += [1]
        print(' '.join(map(str, pascal)))