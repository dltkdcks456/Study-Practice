import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
new_arr = []
for idx, v in enumerate(arr):
    new_arr.append([v, idx])
new_arr.sort()
maxV = 0
for index, value in enumerate(new_arr):
    if maxV < value[1] - index:
        maxV = value[1] - index
print(maxV)