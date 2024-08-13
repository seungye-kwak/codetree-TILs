import sys
n = int(input())
live = list(map(int, input().split()))

min_n = sys.maxsize
for i in range(n) :
    total = 0
    for k in range(n) :
        if k != i :
            total += live[k]*abs(i-k)

    min_n = min(min_n, total)

print(min_n)