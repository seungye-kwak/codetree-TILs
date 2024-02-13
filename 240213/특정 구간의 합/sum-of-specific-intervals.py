n, m = map(int, input().split())
a = list(map(int, input().split()))
def print_sum() :
    for _ in range(m) :
        a1, a2 = map(int, input().split())
        print(sum(a[a1-1:a2]))

print_sum()