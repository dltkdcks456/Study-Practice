import sys
def gdc(a, b):
    if b == 0:
        return a
    return gdc(b, a % b )

T = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(T)]
li.sort()
for i in range(len(li) - 1):
    li[i] = li[i + 1] - li[i]
li.pop(-1)
minV = li[0]
gdc_num = li[0]
for j in li:  
    gdc_num = gdc(gdc_num, j)
    if minV > gdc_num:
        minV = gdc_num
    
for k in range(2, minV + 1):
    if minV % k == 0:
        print(k, end=' ')