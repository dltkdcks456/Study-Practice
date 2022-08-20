import sys

T = int(sys.stdin.readline())
people = {}
for l in range(T):
    a, b = sys.stdin.readline().split()
    if int(a) in people:
        people[int(a)].append(b)
    else:
        people[int(a)] = [b]

age = sorted(people.keys())
for k in age:
    for l in people[k]:
        print(k, l)