'''
사전순 낱말 배열
d > l > r > u
우선, S와 E의 x와 y좌표를 빼고 그 절댓값의 합이 짝수인지 홀수인지 판별한다
짝수라면 k도 짝수가 나와야하며, 홀수이면 k도 홀수가 나와야 목적지에 도달할 수 있다.
0. 반드시 움직여야하는 경로를 우선 q에 넣어둔다.
1. 시작점에서 4군데의 방향을 살펴본다. d -> l -> r -> u 순서로...
2. 우선 q에서 d가 있으면 d를 꺼내서 이동한다
3 - 1. d가 없지만 d로 갈 수 있으면 d를 q에 추가하고, 원복해야하므로 u도 같이 추가한다.
3 - 2. d가 없고 d로도 갈 수 없으면 1번으로 돌아가서 l부터 진행한다.
'''

def solution(n, m, x, y, r, c, k):
    answer=''
    K = k
    X = x
    Y = y

    direction_cnt = {'d' : 0, 'l' : 0, 'r' : 0, 'u' : 0}

    diff_x = r - x
    diff_y = c - y
    Total = abs(diff_x) + abs(diff_y)
    if diff_x < 0:
        direction_cnt['u'] = abs(diff_x)
    else:
        direction_cnt['d'] = diff_x

    if diff_y < 0:
        direction_cnt['l'] = abs(diff_y)
    else:
        direction_cnt['r'] = diff_y

    def move():
        nonlocal answer, X, Y, Total
        if direction_cnt['d'] > 0:
            direction_cnt['d'] -= 1
            answer += 'd'
            X += 1
            return
        elif X + 1 <= n and Total + 2 <= K:
            answer += 'd'
            direction_cnt['u'] += 1
            X += 1
            Total += 2
            return
        elif direction_cnt['l'] > 0:
            direction_cnt['l'] -= 1
            answer += 'l'
            Y -= 1
            return
        elif Y - 1 >= 1 and Total + 2 <= K:
            answer += 'l'
            direction_cnt['r'] += 1
            Y -= 1
            Total += 2
            return
        elif direction_cnt['r'] > 0:
            direction_cnt['r'] -= 1
            answer += 'r'
            Y += 1
            return
        elif Y + 1 <= m and Total + 2 <= K:
            answer += 'r'
            direction_cnt['l'] += 1
            Y += 1
            Total += 2
            return
        elif direction_cnt['u'] > 0:
            direction_cnt['u'] -= 1
            answer += 'u'
            X -= 1
            return
        elif X - 1 >= 1 and Total + 2 <= K:
            answer += 'u'
            direction_cnt['d'] += 1
            X -= 1
            Total += 2
            return

    # impossible인지 먼저 판단
    # 차이값의 절댓값 합이 짝수이면 짝수, 홀수이면 홀수가 나와야한다.
    abs_diff_xy = abs(diff_x) + abs(diff_y)
    if (abs_diff_xy % 2 == 0 and k % 2 == 1) or (abs_diff_xy % 2 == 1 and k % 2 == 0):
        return "impossible"
    if abs_diff_xy > K:
        return "impossible"

    while len(answer) != K:
        move()

    return answer