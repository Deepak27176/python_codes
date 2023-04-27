class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            print("stack is empty")
        else:
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


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.is_empty()
# stack.pop()
# stack.pop()
# stack.pop()

