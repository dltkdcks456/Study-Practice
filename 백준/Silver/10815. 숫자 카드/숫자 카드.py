import sys
num_list = [False] * 20000001
N = int(sys.stdin.readline())
card_list = list(map(int, sys.stdin.readline().split()))

for i in card_list:
    num_list[i] = True

M = int(sys.stdin.readline())
my_card_list = list(map(int, sys.stdin.readline().split()))
result = []
for j in my_card_list:
    if num_list[j] == True:
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))