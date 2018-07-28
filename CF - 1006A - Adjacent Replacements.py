# http://codeforces.com/problemset/problem/1006/A
n = int(input())
array = list(map(int, input().split()))
for i in range(len(array)):
    if array[i] % 2 == 0:
        array[i] -= 1
for i in array:
    print(i, end=" ")
