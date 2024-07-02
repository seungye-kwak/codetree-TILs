# 10의 6승까지, 0 ~ 9 값
MAX_K = 6
MAX_DIGIT = 10

n = int(input())
arr = list(map(int, input().split()))

def radix_sorted() :
    global arr

    p = 1
    for pos in range(MAX_K) :
        arr_new = [[] for _ in range(MAX_DIGIT)] # 0 ~ 9 자릿수
        for elem in arr :
            digit = (elem // p) % 10
            arr_new[digit].append(elem)
        
        arr = []
        for digit in range(MAX_DIGIT):
            for elem in arr_new[digit]:
                arr.append(elem)

        p *= 10

radix_sorted()

print(*arr)