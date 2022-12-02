import sys
from collections import deque

S = input()
T = deque(input())
''' 
signal이 1이면 왼쪽에서부터 읽고
0이면 오른쪽에서 읽어야 한다.
-> 문자열을 뒤집는 것을 최소화
'''
signal = 1

# T를 제거해 나가다가 개수가 같아졌을 때 같은지 확인
while len(T) != len(S):
    # 정방향으로 읽을 경우
    if signal:
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            signal = 0
    # 역방향으로 읽을 경우
    else:
        if T[0] == 'A':
            T.popleft()
        else:
            T.popleft()
            signal = 1

if signal:
    if deque(S) == T:
        print(1)
    else:
        print(0)
else:
    S = deque(S[::-1])
    if S == T:
        print(1)
    else:
        print(0)