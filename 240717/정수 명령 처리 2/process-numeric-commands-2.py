from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def push(self, num) :
        self.q.append(num)

    def empty(self):
        if not self.q :
            return 1
        else :
            return 0


    def pop(self) :
        if self.empty() :
            raise ValueError
        
        else :
            return self.q.popleft()

    def size(self) :
        return len(self.q)

    def front(self) :
        return self.q[0]

n = int(input())
q = Queue()
for _ in range(n) :
    req = input()
    if 'push' in req :
        num = req.split(' ')[-1]
        q.push(num)

    elif req == 'front':
        print(q.front())

    elif req == 'empty':
        print(q.empty())

    elif req == 'pop':
        print(q.pop())

    elif req == 'size':
        print(q.size())

    else :
        raise ValueError