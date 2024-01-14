from collections import deque

items=deque([1,2,3,4,5])

items.appendleft(0)

items.append(6)

items.extend([7,8,9]) #fügt Elemente aus einer aneren Liste hinzu

items.extendleft([33,22,11]) #reversed

items.pop()

items.popleft()

maxVal=deque([1,2,3,4,5,6], maxlen=3)

items[-1]

items[1:4]  #TypeError

items.rotate() #eins nach rechts

print(items)
