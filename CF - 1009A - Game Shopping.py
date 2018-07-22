# http://codeforces.com/problemset/problem/1009/A
n, m = map(int, input().split())
cost = list(map(int, input().split()))
wallet = list(map(int, input().split()))
count = 0
length = list([len(cost), len(wallet)])
length.sort()
for i in range(length[1]):
    try:
        if wallet[0] >= cost[0]:
            count += 1
            wallet.pop(0)
            cost.pop(0)
            continue
        else:
            cost.pop(0)
    except IndexError:
        print(count)
        exit()
print(count)
