import sys
import math

def make_segment(left, right, tree_index):
    if left == right:
        tree[tree_index] = li[left]
        return tree[tree_index]

    mid = (left + right) // 2

    left_value = make_segment(left, mid, tree_index * 2)
    right_value = make_segment(mid + 1, right, tree_index * 2 + 1)

    tree[tree_index] = (left_value * right_value) % 1000000007

    return tree[tree_index]

def update_segment(left, right, tree_index, update_index, update_value):
    if update_index < left or update_index > right:
        return tree[tree_index]

    if left == right:
        tree[tree_index] = update_value
        return tree[tree_index]

    mid = (left + right) // 2

    left_value = update_segment(left, mid, tree_index * 2, update_index, update_value)
    right_value = update_segment(mid + 1, right, tree_index * 2 + 1, update_index, update_value)

    tree[tree_index] = (left_value * right_value) % 1000000007
    return tree[tree_index]

def find_segment(left, right, tree_index, left_index, right_index):
    if right_index < left or left_index > right:
        return 1

    if left_index <= left and right <= right_index:
        return tree[tree_index]

    mid = (left + right) // 2

    left_value = find_segment(left, mid, tree_index * 2, left_index, right_index)
    right_value = find_segment(mid + 1, right, tree_index * 2 + 1, left_index, right_index)

    return (left_value * right_value) % 1000000007

N, M, K = map(int, sys.stdin.readline().split())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))
tree = [0] * 2 ** (int(math.log2(len(li))) + 2)
make_segment(0, len(li) - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update_segment(0, len(li) - 1, 1, b - 1, c)
    elif a == 2:
        print(find_segment(0, len(li) - 1, 1, b - 1, c - 1) % 1000000007)