def preorder(n):
    if n:
        print(chr(n + 64), end = '')
        if ch1[n]:
            preorder(ord(ch1[n]) - 64)
        else:
            preorder(ch1[n])
        if ch2[n]:
            preorder(ord(ch2[n]) - 64)
        else:
            preorder(ch2[n])

def inorder(n):
    if n:
        if ch1[n]:
            inorder(ord(ch1[n]) - 64)
        else:
            inorder(ch1[n])
        print(chr(n + 64), end='')
        if ch2[n]:
            inorder(ord(ch2[n]) - 64)
        else:
            inorder(ch2[n])

def postorder(n):
    if n:
        if ch1[n]:
            postorder(ord(ch1[n]) - 64)
        else:
            postorder(ch1[n])
        if ch2[n]:
            postorder(ord(ch2[n]) - 64)
        else:
            postorder(ch2[n])
        print(chr(n + 64), end='')


N = int(input())
par = [0] * 27
for j in range(65, 91):
    par[j - 64] = chr(j)
ch1 = [0] * 27
ch2 = [0] * 27
for i in range(1, N + 1):
    p, c1, c2 = input().split()
    if c1 != '.':
        ch1[ord(p) - 64] = c1
    if c2 != '.':
        ch2[ord(p) - 64] = c2
preorder(1)
print()
inorder(1)
print()
postorder(1)