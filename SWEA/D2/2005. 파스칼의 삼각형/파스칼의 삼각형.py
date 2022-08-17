for test in range(int(input())):
    pascal = [1]
    N = int(input())
    print(f'#{test + 1}', pascal[0], sep = '\n')
    while len(pascal) < N:
        for i in range(len(pascal) - 1, 0, -1):
            pascal[i] = pascal[i] + pascal[i - 1]
        pascal.append(1)
        print(' '.join(map(str, pascal)))