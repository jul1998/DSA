class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class QueueClass:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first.data

    def enqueue(self, data):
        node = Node(data)
        if self.length == 0:
            self.first = node
            self.last = node
        else:

            self.last.next = node
            self.last = node
            self.length += 1

    def dequeue(self):
        self.first = self.first.next
        self.length -=1



myQ = QueueClass()
myQ.enqueue("harry")
myQ.enqueue("Axel")
myQ.enqueue("Jul")
myQ.enqueue("Ama")



from collections import deque
q = deque()
q.appendleft("Harry")
q.appendleft("John")
q.appendleft("Ama")
q.appendleft("aLSD")
q.appendleft("Cele")
print(q)
q.pop()
print(q)