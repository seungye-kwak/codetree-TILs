n = int(input())
arr = list(map(int, input().split()))

def selection_sorted():
    for i in range(n-1) :
        min_num = i
        for x in range(i, n) :
            if arr[x] < arr[min_num] :
                min_num = x
        arr[i], arr[min_num] = arr[min_num], arr[i]

selection_sorted()

print(*arr)