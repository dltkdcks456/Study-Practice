import sys
input=sys.stdin.readline

def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p and heap[p] < heap[c]:
        heap[c], heap[p] = heap[p], heap[c]
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
        if c + 1 <= last and heap[c] < heap[c + 1]:
            c += 1
        if heap[p] < heap[c]:
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p * 2
        else:
            break
    return temp

N = int(input())
heap = [0] * 100001
last = 0
for _ in range(N):
    x = int(input())
    if x:
        enq(x)
    else:
        print(deq() if last != 0 else 0)