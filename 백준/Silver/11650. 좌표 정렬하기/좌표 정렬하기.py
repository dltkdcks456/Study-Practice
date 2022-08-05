num_list = sorted(list(tuple(map(int, input().split())) for n in range(int(input()))))

for x in num_list:
    print(' '.join(map(str, x)))