import sys
N = sys.stdin.readline()
N_li = list(map(int, sys.stdin.readline().split()))
M = sys.stdin.readline()
M_li = list(map(int, sys.stdin.readline().split()))
N_dict = {}
for i in N_li:
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1
for j in M_li:
    if j in N_dict:
        print(N_dict[j], end = ' ')
    else:
        print(0, end = ' ')