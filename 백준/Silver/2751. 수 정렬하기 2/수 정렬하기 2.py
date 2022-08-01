import sys
N = int(sys.stdin.readline())
num_list = [False] * 2000001
for i in range(N):
    num_list[int(sys.stdin.readline())] = True
print('\n'.join([str(num) for num in range(-1000000 , 1000001) if num_list[num] == True]))
