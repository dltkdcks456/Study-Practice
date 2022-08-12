while True:
    n = list(input())
    if n != ['0']:
        if n[::-1] == n:
            print('yes')
        else:
            print('no')
    else:
        break
    