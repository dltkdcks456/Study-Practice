import sys

def inorder(n):                 # 중위 순회의 루트로 진행
    global i                    # num_list를 입력해주어야하므로 그 해당 인덱스
    if n <= N:
        inorder(2 * n)          # 왼쪽 자식 노드 인덱스
        tree[n] = num_list[i]   # 중간 노드는 해당 자리에 num_list값 입력
        i += 1
        inorder(2 * n + 1)      # 오른쪽 자식 노드 인덱스

input = sys.stdin.readline
K = int(input())                # 깊이
num_list = list(map(int, input().split()))
N = len(num_list)               # 트리의 총 개수 2^k - 1
tree = [0] * (N + 1)            # 트리가 들어갈 공간
i = 0
inorder(1)
for j in range(K):              # 깊이만큼, 즉 지수의 범위 설정
    for k in range(2 ** j, 2 ** (j + 1)):   # 2의 지수가 출발점이자 도착점으로 층마다 출력
        print(tree[k], end = ' ')
    print()