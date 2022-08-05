N = int(input())
num_list = []

for n in range(N):
    num_list.append(tuple(map(int, input().split())))

num_list.sort()

for x in num_list:
    print(' '.join(map(str, x)))