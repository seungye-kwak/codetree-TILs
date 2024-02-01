import math
a, b = map(int, input().split())

def prime_number(num) :
    pn = True
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0 :
            pn = False
    return pn


def even_number(num) :
    en = False
    n = str(num)
    s = 0
    for x in n :
        s += int(x)
    if s%2 == 0 :
        en = True
    return en

cnt = 0
for k in range(a, b+1) :
    if prime_number(k) == True and even_number(k) == True:
        cnt += 1

print(cnt)