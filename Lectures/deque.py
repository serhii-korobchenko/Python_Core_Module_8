from collections import deque # quick add elements in list ---> черга


d = deque()
d.append('last')
d.appendleft('first')
d.insert(1, 'middle')
print(d)            # deque(['first', 'middle', 'last'])

print(d.pop())      # 'last'
print(d.popleft())  # 'first'
print(d)            # deque(['middle'])



# Set up size of list

d = deque(maxlen=5)
for i in range(10):
    d.append(i)

print(d)            # deque([5, 6, 7, 8, 9], maxlen=5)