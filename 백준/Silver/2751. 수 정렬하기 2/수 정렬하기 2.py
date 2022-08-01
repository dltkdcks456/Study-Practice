import sys
N = int(sys.stdin.readline())
num_list = sorted([int(sys.stdin.readline()) for i in range(N)])
print('\n'.join(map(str, num_list)))