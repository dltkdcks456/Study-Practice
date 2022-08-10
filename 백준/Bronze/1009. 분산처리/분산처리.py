dict1 = {1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1], 4: [4, 6], 5: [5], 6: [6], 7: [7, 9, 3, 1], 8: [8, 4, 2, 6], 9: [9, 1], 0: [10]}

T = int(input())
for i in range(T):
    key, repeat = map(int, input().split())
    key = key % 10
    k_li = dict1[key]
    if len(k_li) == 1:
        print(k_li[0])
    else:
        rest = repeat % len(k_li)
        print(k_li[rest - 1])