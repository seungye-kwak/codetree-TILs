n = int(input())

def get_num(n) :
    if n in [0, 1, 2]:
        return n

    return n + get_num(n-2)

print(get_num(n))