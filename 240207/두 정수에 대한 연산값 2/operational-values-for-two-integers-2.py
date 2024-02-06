a, b = map(int, input().split())

def plus_multiple(a,b) :
    f=max(a,b)*2
    s=min(a,b)+10
    if max(a,b) == a :
        return f, s
    else :
        return s, f

print(*plus_multiple(a, b))