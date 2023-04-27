class Stack:
    def __init__(self):
        self.List = []

    def push(self, value):
        self.List.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.List.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.List[len(self.List)-1]

    def isEmpty(self):
        if not self.List:
            return True
        else:
            return False

    def __str__(self):
        values = reversed(self.List)
        val = [str(x) for x in values]
        return "\n".join(val)


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack)
# print(stack.peek())
# print(stack)
# stack.pop()
# stack.pop()
# print(stack)
# print(stack.peek())


