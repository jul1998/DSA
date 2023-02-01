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

    def insert_values(self, data_list):
        #self.head = None
        for data in data_list:
            self.inset_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def remove(self, index):
        if index < 0 or index> self.get_length():
            raise IndexError("Index out of range xD")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index> self.get_length():
            raise IndexError("Index out of range xD")

        if index == 0:
            self.insert_at_beggining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

linkedL = LinkedList()
linkedL.insert_at_beggining(5)
linkedL.insert_at_beggining(14)
linkedL.insert_at_beggining(80)
linkedL.inset_at_end(20)
linkedL.insert_values(["grape", "banana", "orange"])
#linkedL.remove(1)
linkedL.insert_at(3,"hahaha")
print(linkedL.get_length())
linkedL.print()
