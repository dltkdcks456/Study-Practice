
'''
꽂힌 전기용품 중에서 가장 나중에 전기용품으로 사용되는 것부터 제거한다
'''
N, K = map(int, input().split())
machine = list(map(int, input().split()))
multitap = set()
idx = cnt = 0
while idx < K:
    # 멀티탭에 전기 용품을 아직 꽂을 수 있을 경우에는 그냥 꽂는다
    if len(multitap) < N:
        multitap.add(machine[idx])
        idx += 1
        continue
    else:
        # 이번에 사용할 전기용품이 이미 멀티탭에 꽂히면 그냥 지나간다
        if machine[idx] in multitap:
            idx += 1
            continue
        # 멀티탭에 있는 전기용품 중 가장 나중에 사용되는 것을 뽑고 이번 전기용품을 꽂는다
        else:
            maxV = maxV_idx = -1
            for i in multitap:
                for j in range(idx + 1, K):
                    if machine[j] == i and j > maxV_idx:
                        maxV_idx = j
                        maxV = machine[j]
                        break
                    elif machine[j] == i:
                        break
                else:
                    maxV = i
                    break
            multitap.remove(maxV)
            multitap.add(machine[idx])
            idx += 1
            cnt += 1

print(cnt)
