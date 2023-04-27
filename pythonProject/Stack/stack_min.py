class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.min = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.min = self.head.value
        else:
            new_node.next = self.head
            self.head = new_node
            if self.min > new_node.value:
                self.min = new_node.value

    def pop(self):
        if self.head is None:
            print("stack is empty")
        else:
            if self.head.value == self.min:
                self.min = self.head.next.value
                temp = self.head.next
                while temp.next:
                    if temp.value < self.min:
                        self.min = temp.value
                    temp = temp.next
            self.head = self.head.next

    def peek(self):
        if self.head is None:
            print("Stack is empty")
        else:
            print(self.head.value)

    def is_empty(self):
        if self.head is None:
            print("True")
        else:
            print("False")

    def minimum(self):
        print(self.min)

    def __str__(self):
        lis = []
        temp = self.head
        while temp:
            lis.append(temp.value)
            temp = temp.next
        return " ".join(map(str, lis))


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


stack1 = Stack()
stack1.push(7)
stack1.push(2)
stack1.push(4)
stack1.push(3)
stack1.push(5)
stack1.push(1)
stack1.minimum()
stack1.pop()
stack1.minimum()
