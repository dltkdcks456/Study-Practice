import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

# 문제 조건
# 유사 중위 순회를 통해 이동하는 횟수를 출력

# 필요 조건
# 딕셔너리를 통해 노드의 정보 저장
# 재귀를 통해 함수를 만듦
# 횟수의 카운트는 어떻게 해줘야할지 고민이 필요
def inorder1(a):
    if a != -1:
        inorder1(nodes[a][0])
        real_inorder.append(a)
        inorder1(nodes[a][1])


def inorder(n):
    stack = [n]
    visited[n] = 1
    path.append(n)
    while stack:
        v = stack.pop()
        if nodes[v][0] != -1 and visited[nodes[v][0]] == 0:
            stack.append(nodes[v][0])
            path.append(nodes[v][0])
            visited[nodes[v][0]] = 1
        elif nodes[v][1] != -1 and visited[nodes[v][1]] == 0:
            stack.append(nodes[v][1])
            path.append(nodes[v][1])
            visited[nodes[v][1]] = 1
        elif v == end_pos:
            return
        else:
            if par[v]:
                stack.append(par[v])
                path.append(par[v])


N = int(input())
nodes = {i : [-1, -1] for i in range(1, N + 1)}
visited = [0] * (N + 1)
visited[0] = 1
par = [0] * (N + 1)
for _ in range(N):
    node, left, right = map(int, input().split())
    nodes[node] = [left, right]
    if left != -1:
        par[left] = node
    if right != -1:
        par[right] = node
path = []
real_inorder = []

inorder1(1)
# print(real_inorder)

end_pos = real_inorder[-1]
inorder(1)
# print(path)
# # print(par)
# # print(end_pos)
# # print(path)
print(len(path) - 1)