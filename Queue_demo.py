# Queue FIFO list

import collections
q = collections.deque( )
q.append('Suhana')
q.append('Shabana')
q.append('Shakila')
q.append('Shakira')
q.append('Sameera')
print(q)
print(q.popleft( ))
print(q.popleft( ))
print(q.popleft( ))
print(q)