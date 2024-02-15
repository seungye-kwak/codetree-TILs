def power_num(n) :
    if n < 10 :
        return n ** 2
    return power_num(n//10) + power_num(n%10)

n = int(input())
print(power_num(n))