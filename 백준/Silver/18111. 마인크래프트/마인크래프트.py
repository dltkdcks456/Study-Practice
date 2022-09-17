import sys
N, M, B = map(int, sys.stdin.readline().split())
li = []

for _ in range(N):
    li.extend(map(int, sys.stdin.readline().split()))
    
minT = 500 * 500 * 256
maxH = 0

for h in range(min(li), max(li) + 1):
    minus_total = plus_total = time = 0
    for i in li:
        diff = i - h
        if diff > 0:
            plus_total += diff
        elif diff < 0:
            minus_total += diff
            
    if plus_total + B >= -minus_total:
        time += - minus_total + plus_total * 2
    else:
        break
    
    if time < minT:
        minT = time
        maxH = h
    elif time == minT:
        if h > maxH:
            maxH = h

print(minT, maxH)