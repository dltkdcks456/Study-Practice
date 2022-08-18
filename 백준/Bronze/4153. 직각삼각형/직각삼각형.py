while True:
    line = list(map(int, input().split()))
    if line != [0, 0, 0]:
        num = sorted(line)
        line1 =num[0] ** 2
        line2 =num[1] ** 2
        line3 = num[-1] ** 2
        if line3 == line1 + line2:
            print('right')
        else:
            print('wrong')
    else:
        break