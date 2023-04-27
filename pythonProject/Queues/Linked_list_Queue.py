class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value=value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f"{value} is added to queue")
        else:
            self.tail.next = new_node
            self.tail = new_node
            print(f"{value} is added to queue")

    def pop(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print(f"{self.head.value} removed from queue")
            self.head = self.head.next

    def isEmpty(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print("Queue is not empty")

    def peek(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print(f"{self.head.value} is in front of queue")

    def __str__(self):
        if self.head is None:
            return "Queue is empty"
        else:
            temp = self.head
            val = ""
            while temp:
                val = val + "".join(str(temp.value))+" "
                temp = temp.next
            return val


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue)
queue.pop()
queue.peek()
print(queue)
queue.isEmpty()