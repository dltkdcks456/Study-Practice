import sys
def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2        

def deq():
    global last
    temp = heap[1]
    heap[1] = heap[last]
    last -= 1
    p = 1
    c = p * 2
    while c <= last:
        if c + 1 <= last and heap[c] > heap[c + 1]:
            c += 1
        if heap[p] > heap[c]:
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2
        else:
            break
    return temp    

N = int(sys.stdin.readline())
heap = [0] * 100001
last = 0
for _ in range(N):
    data = int(sys.stdin.readline())
    if data == 0:
        if last == 0:
            print(0)
        else:
            print(deq())
    else:
        enq(data)
            