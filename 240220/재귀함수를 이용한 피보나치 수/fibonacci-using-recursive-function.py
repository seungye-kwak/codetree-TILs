def pivonachi(n) :
    if n in [1, 2] :
        return 1
    return pivonachi(n-1)+pivonachi(n-2)

n = int(input())
print(pivonachi(n))