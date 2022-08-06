import sys
num_list = sorted(list(tuple(map(int, sys.stdin.readline().split())) for n in range(int(sys.stdin.readline()))))

for x in num_list:
    print(' '.join(map(str, x)))