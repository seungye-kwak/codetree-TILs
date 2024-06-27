# python은 이중연결리스트 구현체에 해당하는 list라는 class가 따로 없음

class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) :
        self.head = None
        self.tail = None
        self.node_num = 0

    def push_front(self, new_data) :
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head != None :
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        else :
            self.head = new_node
            self.tail = new_node
            new_node.prev = None

        self.node_num += 1

    def push_back(self, new_data) :
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail != None :
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None

        else :
            self.tail = new_node
            self.head = new_node
            new_node.next = None
        
        self.node_num += 1

    def pop_front(self) :
        if self.head == None:
            raise ValueError

        elif self.head.next == None :
            temp = self.head

            self.head = None
            self.tail = None
            self.node_num = 0
            print(temp.data)

        else :
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.node_num -= 1
            print(temp.data)

    def pop_back(self):
        if self.tail == None :
            raise ValueError

        elif self.tail.prev == None:
            temp = self.tail

            self.head = None
            self.tail = None
            self.node_num = 0

            print(temp.data)

        else :
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.node_num -= 1
            print(temp.data)

    def size(self):
        print(self.node_num)

    def empty(self):
        if self.node_num == 0 :
            print(1)
        else :
            print(0)

    def front(self):
        if self.head == None :
            raise ValueError

        else :
            print(self.head.data)

    def back(self):
        if self.tail == None:
            raise ValueError
        else :
            print(self.tail.data)



n = int(input())
dll = DoublyLinkedList()
for _ in range(n) :
    req = input()

    if 'push_front' in req :
        nn = int(req.split(' ')[1])
        dll.push_front(nn)

    elif 'push_back' in req :
        nn = int(req.split(' ')[1])
        dll.push_back(nn)

    elif 'pop_front' in req :
        dll.pop_front()

    elif 'pop_back' in req :
        dll.pop_back()

    elif 'size' in req :
        dll.size()

    elif 'empty' in req :
        dll.empty()

    elif 'front' in req :
        dll.front()

    elif 'back' in req :
        dll.back()
    
    else :
        raise ValueError