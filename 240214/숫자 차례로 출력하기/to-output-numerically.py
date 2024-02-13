n = int(input())
cnt = 2
def print_seq(cnt) :
    if cnt == 0:
        return
    print_seq(cnt-1)
    if cnt == 1:
        print(*[x for x in range(1, n+1)])
    else :
        print(*[x for x in reversed(range(1, n+1))])
    cnt -= 1

print_seq(cnt)