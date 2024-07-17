from collections import deque

n, k = map(int, input().split())
q = deque([x for x in range(1,n+1)])

while len(q) > 1:
    for _ in range(k-1) :
        q.append(q[0])
        q.popleft()
    print(q[0], end=' ')
    q.popleft()

print(q[0], end = ' ')