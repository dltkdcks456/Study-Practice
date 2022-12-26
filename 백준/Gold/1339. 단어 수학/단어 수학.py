import sys
input = sys.stdin.readline

'''
1. 순열을 활용
알파벳을 모두 모은 다음 순열을 통해 각 알파벳에 숫자를 대응시킨다.
그 후 숫자를 합하면서 maxV보다 작으면 리턴하는 백트래킹을 활용한다.
백트래킹 활용이 내가 구현한 부분에서는 까다로우며 비효율적

2. 그리디를 이용해서 문제 풀이
'''

N = int(input())
alpha = [[] for _ in range(8)]
alpha_pos = dict()
for _ in range(N):
    text = input().rstrip()
    idx = 0
    for char in text[::-1]:
        alpha[idx].append(char)
        idx += 1

idx_alpha = 0
for x in alpha:
    if x:
        for y in x:
            if y in alpha_pos:
                alpha_pos[y] += 10 ** idx_alpha
            else:
                alpha_pos[y] = 10 ** idx_alpha
        idx_alpha += 1

sum_arr = []
for v in alpha_pos.values():
    sum_arr.append(v)
sum_arr.sort(reverse=True)

maxV = 0
i = 9
for w in sum_arr:
    maxV += w * i
    i -= 1
print(maxV)