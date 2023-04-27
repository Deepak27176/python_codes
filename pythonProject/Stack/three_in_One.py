class MultiStack:
    def __init__(self, maxsize):
        self.no_of_stacks = 3
        self.stack_list = [None]*(self.no_of_stacks*maxsize)
        self.stack_sizes = [0]*self.no_of_stacks
        self.maxsize = maxsize

    def isFull(self, stack_no):
        if self.stack_sizes[stack_no] == self.maxsize:
            return True
        else:
            return False

    def isEmpty(self, stack_no):
        if self.stack_sizes[stack_no] == 0:
            return True
        else:
            return False

    def onTop(self, stack_no):
        offset = stack_no*self.maxsize
        return offset + self.stack_sizes[stack_no]-1

    def push(self, stack_no, value):
        if self.isFull(stack_no=stack_no):
            print(f"stack{stack_no} is full")
        else:
            self.stack_sizes[stack_no] += 1
            self.stack_list[self.onTop(stack_no=stack_no)] = value

    def pop(self, stack_no):
        if self.isEmpty(stack_no=stack_no):
            print(f"Stack{stack_no} is empty")
        else:
            print(f"{self.stack_list[self.onTop(stack_no=stack_no)]} popped out")
            self.stack_list[self.onTop(stack_no=stack_no)] = None
            self.stack_sizes[stack_no] -= 1

    def display(self):
        print(self.stack_list)


ms = MultiStack(3)
ms.push(0, 0)
ms.push(1, 0)
ms.push(2, 0)
ms.push(0, 1)
ms.push(1, 1)
ms.push(2, 1)
ms.push(0, 2)
ms.push(1, 2)
ms.push(2, 2)
print([ms.isFull(i) for i in range(3)])
ms.display()