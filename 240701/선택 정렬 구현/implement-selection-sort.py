n = int(input())
arr = list(map(int, input().split()))

def selection_sorted():
    for i in range(n-1):
        min_i = i
        for x in range(i+1, n):
            if arr[min_i] > arr[x] :
                min_i = x

        arr[i], arr[min_i] = arr[min_i], arr[i]

selection_sorted()

print(*arr)