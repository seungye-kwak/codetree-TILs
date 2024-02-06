a, b = map(int, input().split())

def plus_multiple(a,b) :
    f=max(a,b)*2
    s=min(a,b)+10
    return s, f

print(*plus_multiple(a, b))