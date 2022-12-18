import sys
from collections import deque
input = sys.stdin.readline

'''
0의 위치를 모두 기록해두고 공기와 맞닿는 부분은 2로 변경시켜준다.
자기 자신도 2로 되면서 주변에 있는 치즈들도 공기와 맞닿아 있으므로 큐에 추가해준다
이런식으로 하나씩 제거해나가기
'''

def air(r, c):
    '''
    바깥 공기와 닿는 부분을 2로 변경
    '''
    q = deque()
    q.append([r, c])
    while q:
        ri, ci = q.popleft()
        arr[ri][ci] = 2
        for d in range(4):
            nr = ri + dr[d]
            nc = ci + dc[d]
            if cnt % 2 != 0:
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == 1 and (nr, nc) not in cheese1:
                        cheese1.add((nr, nc))
                    elif arr[nr][nc] == 0:
                        arr[nr][nc] = 2
                        q.append([nr, nc])
            else:
                if 0 <= nr < N and 0 <= nc < M:
                    if arr[nr][nc] == 1 and (nr, nc) not in cheese:
                        cheese.add((nr, nc))
                    elif arr[nr][nc] == 0:
                        arr[nr][nc] = 2
                        q.append([nr, nc])

def cheese_melten():
    # 녹아없어질 치즈 개수
    if cnt % 2 != 0:
        while cheese:
            cheese_r, cheese_c = cheese.pop()
            arr[cheese_r][cheese_c] = 2
            for d in range(4):
                nr = cheese_r + dr[d]
                nc = cheese_c + dc[d]
                if arr[nr][nc] == 1 and (nr, nc) not in cheese and (nr, nc) not in cheese1:
                    cheese1.add((nr, nc))
                elif arr[nr][nc] == 0 and (nr, nc) not in inner_air:
                    inner_air.add((nr, nc))
    else:
        while cheese1:
            cheese_r, cheese_c = cheese1.pop()
            arr[cheese_r][cheese_c] = 2
            for d in range(4):
                nr = cheese_r + dr[d]
                nc = cheese_c + dc[d]
                if arr[nr][nc] == 1 and (nr, nc) not in cheese and (nr, nc) not in cheese1:
                    cheese.add((nr, nc))
                elif arr[nr][nc] == 0 and (nr, nc) not in inner_air:
                    inner_air.add((nr, nc))

if __name__ == '__main__':
    N, M = map(int, input().split())    # N: 세로, M:가로길이
    arr = [list(map(int, input().split())) for _ in range(N)]   # 치즈가 놓여있는 공간
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    # 우선 가장 바깥 테두리는 공기 중에 있으므로 0 -> 2로 변경시켜준다.
    # 공기와 맞닿아 있는 치즈는 녹아없어질 공간에 추가해준다.

    cheese = set()
    cheese1 = set()
    inner_air = set()


    # for i in arr:
    #     print(i)
    # print(cheese)
    cnt = 1
    air(0, 0)
    last_cheese = 0
    while True:
        if cnt % 2 != 0:
            last_cheese = len(cheese)
            # print(cheese)
            cheese_melten()
            while inner_air:
                air_r, air_c = inner_air.pop()
                if arr[air_r][air_c] != 2:
                    air(air_r, air_c)
            if not cheese1:
                break
        else:
            last_cheese = len(cheese1)
            # print(cheese1)
            cheese_melten()
            while inner_air:
                air_r, air_c = inner_air.pop()
                if arr[air_r][air_c] != 2:
                    air(air_r, air_c)
            if not cheese:
                break
        cnt += 1
        # for i in arr:
        #     print(i)
        # print('-----------------------------')
    print(cnt - 1)
    print(last_cheese)