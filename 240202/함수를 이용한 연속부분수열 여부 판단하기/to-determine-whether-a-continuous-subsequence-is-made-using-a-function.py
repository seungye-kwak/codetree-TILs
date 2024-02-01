n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def part_seq(a, b) :
    if len(a) > len(b) :
        lst1, lst2 = a, b
    elif len(a) == len(b) :
        if a == b :
            return 'Yes'
    else :
        lst1, lst2 = b, a

    if lst2[0] not in lst1 :
        return 'No'
    
    start = lst1.index(lst2[0])
    mini_lst1 = lst1[start:start+len(lst2)]
    if mini_lst1 == lst2 :
        return 'Yes'
    else :
        return 'No'

print(part_seq(a, b))