import sys
import math

def segment(left, right, tree_index):
    if left == right:
        tree[tree_index] = li[left]
        return tree[tree_index]

    mid = (left + right) // 2

    left_tree = segment(left, mid, tree_index * 2)
    right_tree = segment(mid + 1, right, tree_index * 2 + 1)

    tree[tree_index] = left_tree + right_tree

    return tree[tree_index]

def update_seg(left, right, tree_index, update_value, update_index):
    if left > update_index or right < update_index:
        return tree[tree_index]

    if left == right:
        tree[tree_index] = update_value
        return tree[tree_index]

    mid = (left + right) // 2

    left_tree = update_seg(left, mid, tree_index * 2, update_value, update_index)
    right_tree = update_seg(mid + 1, right, tree_index * 2 + 1, update_value, update_index)

    tree[tree_index] = left_tree + right_tree

    return tree[tree_index]

def find_seg(left, right, tree_index, left_index, right_index):
    if left > right_index or right < left_index:
        return 0

    if left >= left_index and right <= right_index:
        return tree[tree_index]
    mid = (left + right) // 2

    left_value = find_seg(left, mid, tree_index * 2, left_index, right_index)
    right_value = find_seg(mid + 1, right, tree_index * 2 + 1, left_index, right_index)

    return left_value + right_value

N, M, K = map(int, sys.stdin.readline().split())
li = []
for _ in range(N):
    li.append(int(sys.stdin.readline()))
tree = [0] * 2 ** (int(math.log2(len(li))) + 2)
segment(0, len(li) - 1, 1)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update_seg(0, len(li) - 1, 1, c, b - 1)
    elif a == 2:
        print(find_seg(0, len(li) - 1, 1, b - 1, c - 1))