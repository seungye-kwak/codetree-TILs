n = int(input())
lst = []
for _ in range(n) :
    req = input()
    if 'push_back' in req :
        n = int(req.split(' ')[1])
        lst.append(n)
    elif 'pop_back' in req :
        lst = lst[:-1]
    elif 'size' in req :
        print(len(lst))
    elif 'get' in req :
        n = int(req.split(' ')[1])
        print(lst[n-1])