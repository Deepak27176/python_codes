class Queue:
    def __init__(self):
        self.List = []

    def enqueue(self, value):
        self.List.append(value)
        print(f"{value} is added to Queue")

    def dequeue(self):
        print(f"{self.List[0]} is dequeued")
        self.List.remove(self.List[0])

    def __str__(self):
        return " ".join(map(str, self.List))

    def peek(self):
        if not self.List:
            print("Queue is empty")
        else:
            print(self.List[0])

    def is_empty(self):
        if not self.List:
            print("yes queue is empty")
        else:
            print("Queue is not empty")


# Q1 = Queue()
# Q1.enqueue(1)
# Q1.enqueue(2)
# Q1.enqueue(3)
# print(Q1)
# Q1.dequeue()

