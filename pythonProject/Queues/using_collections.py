from collections import deque

queue = deque(maxlen=3)
queue.append(1)
queue.append(3)
queue.append(5)
print(*queue)
queue.append(6)
print(*queue)