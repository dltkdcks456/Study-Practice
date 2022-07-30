n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))
for j in sorted(num_list):
    print(j)