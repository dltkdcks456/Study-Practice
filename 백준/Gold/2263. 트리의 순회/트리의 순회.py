import sys
sys.setrecursionlimit(10 ** 5)

def tree(In_L, In_R, Post_L, Post_R):
    center = postorder[Post_R]
    print(center, end = ' ')
    left_length = right_length = 0
    for i in range(In_L, In_R + 1):
        if inorder[i] == center:
            left_length = i - In_L
            right_length = In_R - i
            break
    if left_length:
        tree(In_L, i - 1, Post_L, Post_L + left_length - 1)
    if right_length:
        tree(i + 1, In_R, Post_R - right_length, Post_R - 1)


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
tree(0, n - 1, 0, n - 1)
