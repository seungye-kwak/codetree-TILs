y, m, d = map(int, input().split())

def right_date(y, m, d) :
    if m == 2 :
        if y%4==0 :
            if y%100 == 0 and y%400 != 0:
                max_d = 28
            else :
                max_d = 29
        else :
            max_d = 28
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        max_d = 31
    elif m in [4, 6, 9, 11]:
        max_d = 30
    else :
        max_d = 0
    
    return max_d

def print_season(y, m, d) :
    max_d = right_date(y, m, d)
    if max_d ==0 or max_d<d :
        return -1
    
    else :
        if 3<=m<=5 :
            return 'Spring'
        elif 6<=m<=8 :
            return 'Summer'
        elif 9<=m<=11 :
            return 'Fall'
        elif m==12 or 1<=m<=2 :
            return 'Winter'
        else :
            return -1

print(print_season(y, m, d))