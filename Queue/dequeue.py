# Deque implementaion in python

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


d = Deque()
print("Check Deque is empty", d.isEmpty())
d.addRear(8)
print(f"Add in Rear Deque is {8}, {d.items} ")
d.addRear(5)
print(f"Add in Rear Deque is {5}, {d.items} ")
d.addFront(7)
print(f"Add in Front Deque is {7}, {d.items} ")
d.addFront(10)
print(f"Add in Front Deque is {10}, {d.items} ")
print("Size", d.size())
print("Check Empty or not", d.isEmpty())
d.addRear(11)
print(f"Add in Rear Deque is {11}, {d.items} ")
print("Remove Rear:", d.removeRear())
print("After Remove Rear:", d.items )
print("Remove Front", d.removeFront())
print("After Remove Front:", d.items )
d.addFront(55)
print(f"Add in Front Deque is {55}, {d.items} ")
d.addRear(45)
print(f"Add in Rear Deque is {45}, {d.items} ")
print("Final Result", d.items)
