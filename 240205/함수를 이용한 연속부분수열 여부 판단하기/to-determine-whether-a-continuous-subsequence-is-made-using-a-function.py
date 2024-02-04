n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def part_seq(a, b) :
    if len(a) == len(b) and a != b :
        return 'No'
    
    if len(a) > len(b) :
        longs, shorts = a, b
    else :
        longs, shorts = b, a

    answer = 'No'
    while shorts[0] in longs:
        start = longs.index(shorts[0])
        if longs[start:start+len(shorts)] == shorts :
            answer = 'Yes'
            break
        else :
            longs.remove(shorts[0])
    
    return answer

print(part_seq(a, b))