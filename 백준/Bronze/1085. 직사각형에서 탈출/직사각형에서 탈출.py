import sys
x, y, w, h = map(int,sys.stdin.readline().split())
dis_list = [x, y, w - x, h - y]
print(min(dis_list))