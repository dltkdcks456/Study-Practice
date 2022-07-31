import sys
num_list = [(int(sys.stdin.readline())) for i in range(int(sys.stdin.readline()))]  
print('\n'.join(map(str, sorted(num_list))))