a, b = map(int, input().split())

def game(a, b) :
    cnt=0
    for i in range(a, b+1) :
        if i%3 == 0 :
            cnt += 1
        else :
            for x in ['3', '6', '9'] :
                if x in str(i) :
                    cnt += 1
                    break
    return cnt

print(game(a, b))