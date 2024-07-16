class Stack :
    def __init__(self):
        self.item = []

    def push(self, num):
        self.item.append(num)

    def empty(self) :
        if self.item == [] :
            return 1
        else :
            return 0

    def pop(self) :
        if self.empty() == 1 :
            raise ValueError

        else :
            return self.item.pop()

    def top(self) :
        if self.empty() == 1:
            raise ValueError

        else :
            return self.item[-1]

    def size(self) :
        return len(self.item)

n = int(input())
s = Stack()
for _ in range(n) :
    req = input()
    if 'push' in req :
        num = req.split(' ')[-1]
        s.push(num)
    elif 'size' in req :
        print(s.size())

    elif 'empty' in req :
        print(s.empty())

    elif 'pop' in req :
        print(s.pop())
    
    elif 'top' in req :
        print(s.top())

    else :
        raise ValueError("잘못된 명령어")