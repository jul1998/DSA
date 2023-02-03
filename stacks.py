class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self, top=None, bottom=None):
        self.top = top
        self.length = 0

    def peek(self):
        print(self.top.data)
        return

    def push(self,data):
        node = Node(data, self.top)
        if self.length == 0:
            self.top = node
            self.length += 1
            return

        pointer = self.top
        self.bottom = pointer
        self.top = node
        self.top.next = pointer
        self.length += 1
        return self

    def pop(self):
        if self.top == None:
            raise Exception("Stack is empty")
        self.top = self.top.next
        self.length -= 1

    def print(self):
        if self.top == None:
            raise Exception("Stack is empty")
        itr = self.top
        stackList = ""
        while itr:
            stackList += str(itr.data) + "-->"
            itr = itr.next
        print(stackList)

myStack = Stack()

myStack.push("Youtube")
myStack.push("Udemy")
myStack.push("Faceb")
myStack.push("SSS")
myStack.push("DDDD")
myStack.peek()
myStack.print()
print(myStack.length)



from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        return self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

newStack = Stack()
newStack.push("Facebook")
newStack.push("Wikipedia")
newStack.push("Amazon")
print(newStack.peek())
print(newStack.container)
newStack.pop()
print(newStack.size())
print(newStack.is_empty())
print(newStack.container)
