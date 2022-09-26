import sys

N = int(sys.stdin.readline())
line = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
line.sort()
s, e = line[0]
sumV = 0

if len(line) == 1:
    sumV = e - s
else:
    for i in range(1, len(line)):
        ns, ne = line[i]
        if ns <= e:
            e = max(e, ne)
            if i == N - 1:
                sumV += e - s
        else:
            sumV += e - s
            s, e = ns, ne
            if i == N - 1:
                sumV += e - s
print(sumV)