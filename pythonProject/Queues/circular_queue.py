class CircularQueue:
    def __init__(self, size):
        self.list = size*[None]
        self.top = -1
        self.start = 0
        self.size = size
        self.count = 0

    def isFull(self):
        if self.count == self.size:
            return True
        else:
            return False

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def enQueue(self, value):
        if self.isFull():
            print("Queue is Full")
        else:
            self.top = (self.top+1) % self.size
            self.list[self.top] = value
            self.count += 1
            print(f"{value} is inserted at end of queue")

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(f"{self.list[self.start]} is deQueued")
            self.start = (self.start + 1) % self.size
            self.count -= 1

    def __str__(self):
        values = ""
        if self.count == 0:
            return "Queue is Empty"
        else:
            f1 = self.start
            for i in range(1, self.count+1):
                values = values +"".join(str(self.list[f1]))+" "
                f1 = (f1+1) % self.size
            return values

    def peek(self):
        if self.count == 0:
            print("Queue is empty")
        else:
            print(f'{self.list[self.start]} is in front of queue')


cQ = CircularQueue(3)
cQ.enQueue(6)
cQ.enQueue(5)
cQ.enQueue(3)
cQ.peek()
print(cQ)
cQ.deQueue()
cQ.peek()
cQ.deQueue()
print(cQ)
cQ.deQueue()
print(cQ)
cQ.enQueue(5)
cQ.enQueue(3)
print(cQ)
