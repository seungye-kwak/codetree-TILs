string = input()

result = 0
sum_ = 0
for s in string :
    if s == '(':
        result += 1
    else :
        sum_ += result

print(sum_)