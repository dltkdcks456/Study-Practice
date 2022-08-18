N = 9
people = [int(input()) for _ in range(N)]
#방법 1
result = []
for i in range(N - 7 + 1):
    for j in range(i + 1, N - 6 + 1):
        for k in range(j + 1, N - 5 + 1):
            for l in range(k + 1, N - 4 + 1):
                for m in range(l + 1, N - 3 + 1):
                    for n in range(m + 1, N - 2 + 1):
                        for o in range(n + 1, N - 1 + 1):
                            # print(i, j, k, l, m, n, o, end =' ')
                            # print()
                            if people[i] + people[j] + people[k] + people[l] + people[m] + people[n] + people[o] == 100:
                                result.append(people[i])
                                result.append(people[j])
                                result.append(people[k])
                                result.append(people[l])
                                result.append(people[m])
                                result.append(people[n])
                                result.append(people[o])
                                print(*sorted(result), sep= '\n')
                                exit()
