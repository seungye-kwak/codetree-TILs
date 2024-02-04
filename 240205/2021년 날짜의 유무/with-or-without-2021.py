m, d = map(int, input().split())

def is_date(m, d) :
    answer = 'Yes'
    if m == 2 :
        if d>28 :
            answer = 'No'
    elif m in [1, 3, 5, 7, 8, 10, 12]:
        if d>31 :
            answer = 'No'
    elif m in [4, 6, 9, 11] :
        if d > 30 :
            answer = 'No'
    else :
        answer = 'No'
    
    return answer

print(is_date(m, d))