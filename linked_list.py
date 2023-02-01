class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        linkedListStr = ""
        while itr:
            linkedListStr += str(itr.data) + "-->"
            itr = itr.next
        print(linkedListStr)

    def inset_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

linkedL = LinkedList()
linkedL.insert_at_beggining(5)
linkedL.insert_at_beggining(14)
linkedL.insert_at_beggining(80)
linkedL.inset_at_end(20)
linkedL.print()
