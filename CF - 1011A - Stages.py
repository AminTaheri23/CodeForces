n, k = input().split()
n = int(n)
k = int(k)
inputed = list(input())
inputed.sort()
out = [inputed[0]]
i = 0


def SumOfAscii(a):
    x = 0
    for j in range(len(a)):
        x += ord(a[j]) - 96
    return x


while len(out) != k and len(out) <= n:
    try:
        i += 1
        if ord(inputed[i]) > ord(out[len(out) - 1]) + 1:
            out.append(inputed[i])
    except IndexError:
        print(-1)
        exit()

print(SumOfAscii(out))
