n = int(input())
arr = list(map(int, input().split()))

def insert_sorted():
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            if arr[j] > key :
                arr[j+1] = arr[j]
                arr[j] = key
                j -= 1

insert_sorted()

print(*arr)