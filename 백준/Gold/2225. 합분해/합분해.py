import sys
input = sys.stdin.readline

'''
조합을 활용해서 N이 주어질 경우 K개 이하로 자르는 방식으로 구할 예정
즉 K분할 되는 경우, K-1 분할 되는 경우의 수 ...과 같이 나누어 합하면 답을 구할 수 있다.
'''

#조합에 대한 함수(nCm)
def comb(n, m):
    temp = 1
    for i in range(m):
        temp *= n - i
    for j in range(1, m + 1):
        temp //= j
    return temp


N, K = map(int, input().split()) # 합의 크기 N, 개수 K
ans = 0
for k in range(K - 1, -1, -1):
    ans += comb(N - 1, k) * comb(K, K - k - 1)
print(ans % 1000000000)