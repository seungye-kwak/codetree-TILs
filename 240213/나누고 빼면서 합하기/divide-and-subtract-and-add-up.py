n, m = map(int, input().split())
a = list(map(int, input().split()))

def seq_add() :
    global m
    # m 이 1이 되기 전까지 m이 홀수면 1을 빼고, 짝수면 2로 나누는 걸 반복
    # A의 m번째 원소를 계속 더해 출력하는 프로그램 작성
    total = 0
    while m >= 1 :
        num = a[m-1]
        total += num
        if m%2==1 :
            m = m-1
        else :
            m = m//2
    return total

print(seq_add())