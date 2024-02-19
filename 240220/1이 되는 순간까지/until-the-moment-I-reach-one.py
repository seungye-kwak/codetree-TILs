n = int(input())

def get_num(n) :
    if n == 1:
        return 0

    if n%2 == 0:
        return get_num(n//2) + 1
    else :
        return get_num(n//3) + 1

print(get_num(n))