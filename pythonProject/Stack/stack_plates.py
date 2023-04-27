class StackOfPlates:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack = [[]]

    def push(self, value):
        if len(self.stack) > 0 and (len(self.stack[-1])) < self.stack_size:
            self.stack[-1].append(value)

        else:
            self.stack.append([value])

    def pop(self):
        while len(self.stack) and len(self.stack[-1]) == 0:
            self.stack.pop()
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1].pop()

    def display(self):
        print(self.stack)


s = StackOfPlates(3)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(3)
s.push(4)
s.display()
s.pop()
s.pop()
s.pop()
s.pop()
s.display()