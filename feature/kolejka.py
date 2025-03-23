from collections import deque
from typing import Deque

q = deque()

q.append("Ala")
q.append("Bogdan")
q.appendleft("Start")

print(q)
print(q.pop())
print(q.popleft())

d = deque([1, 2, 3, 4, 5], maxlen=6)
d.rotate(2)
print(d)
d.rotate(-1)
print(d)
d.append(11)
d.append(111)
print(d)

# typowanie działa
deq2: Deque[str] = deque()
