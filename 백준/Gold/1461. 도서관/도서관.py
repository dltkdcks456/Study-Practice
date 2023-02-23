'''
음수와 양수로 나눠서 받을 예정(부호가 바뀌게 되면 어떻게든 원점을 지나야 하기 때문이다.)
묶음을 통해 가장 바깥부터 합해서 다시 데이터를 정제하고
값이 낮은 것부터 곱하기 2를 해주고 가장 나중에 값이 큰 녀석을 더해준다.
'''
from collections import deque

if __name__=='__main__':
    N, M = map(int, input().split())
    books = list(map(int, input().split()))
    books.sort()

    positive_integer = deque()
    negative_integer = deque()

    for i in range(N):
        if books[i] < 0:
            negative_integer.append(books[i])
        else:
            positive_integer.appendleft(books[i])
    
    # print(positive_integer)
    # print(negative_integer)

    move_distance = []
    for x in range(0, len(negative_integer), M):
        move_distance.append(-negative_integer[x])
    for y in range(0, len(positive_integer), M):
        move_distance.append(positive_integer[y])
    
    # print(move_distance)
    maxV = max(move_distance)
    ans = sum(move_distance) * 2 - maxV
    print(ans)