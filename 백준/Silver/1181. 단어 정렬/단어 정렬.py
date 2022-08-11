import sys
N = int(sys.stdin.readline())
text_list = sorted(set(sys.stdin.readline() for i in range(N)))
text_list.sort(key = len)
print(''.join(text_list))