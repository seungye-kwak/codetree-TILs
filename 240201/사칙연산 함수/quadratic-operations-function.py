a, o, c = input().split()
def cal(a, o, c) :
    if o not in ['+', '-', '*', '/'] :
        return False 
    a, c = int(a), int(c)
    if o == '+' :
        r = a + c
    elif o == '-' :
        r = a - c
    elif o == '*' :
        r = a * c
    else :
        r = a//c

    return f'{a} {o} {c} = {r}'

print(cal(a,o,c))