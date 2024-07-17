from collections import deque

class Deque :
    def __init__(self) :
        self.dq = deque()

    def push_front(self, num):
        self.dq.appendleft(num)

    def push_back(self, num):
        self.dq.append(num)

    def size(self) :
        return len(self.dq)

    def empty(self) :
        if self.size == 0:
            return 1
        else :
            return 0

    def pop_front(self):
        if self.size==0:
            raise ValueError

        else:
            return self.dq.popleft()

    def pop_back(self):
        if self.size==0:
            raise ValueError

        else:
            return self.dq.pop()

    def front(self):
        return self.dq[0]

    def back(self):
        return self.dq[-1]

n = int(input())
dq = Deque()
for _ in range(n) :
    req = input()

    if 'push' in req:
        num = req.split(' ')[-1]
        if 'back' in req:
            dq.push_back(num)

        elif 'front' in req :
            dq.push_front(num)

    elif 'pop' in req:
        if 'back' in req:
            print(dq.pop_back())

        else :
            print(dq.pop_front())

    elif 'size' in req:
        print(dq.size())

    elif 'empty' in req:
        print(dq.empty())

    elif 'front' in req :
        print(dq.front())

    elif 'back' in req:
        print(dq.back())