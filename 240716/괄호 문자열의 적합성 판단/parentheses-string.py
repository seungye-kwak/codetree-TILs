req = input()
req_lst = [x for x in req]

def right_req() :
    stack = []
    for i in range(len(req_lst)) :
        if req_lst[i] == '(':
            stack.append(req_lst[i])
        else :
            if stack :
                return 'No'
            else :
                stack.pop()

    if stack :
        return 'Yes'
    else :
        return 'No'

print(right_req())