class Node:
    def __init__(self, value):
        self.value = value
        self.next_value = None


class LinkedList:
    def __init__(self, value):
        self.head = {
            "value": value,
            "next_value": None
        }
        self.tail = self.head  # It is head because there is only 1 element at the beginning
        self.length = 1

    def append(self, value):
        newNode = {
            "value": value,
            "next_value": None
        }
        self.tail["next_value"] = newNode
        self.tail = newNode
        self.length += 1
        return self.head

    def preaprend(self, value):
        newNode = {"value": value, "next_value": self.head}

        self.head = newNode
        self.length += 1

    def print_list(self):
        newArr = []
        current_node = self.head
        while current_node != None:
            newArr.append(current_node["value"])
            current_node = current_node["next_value"]
        return newArr

    def insert(self, index, value):
        if index >= self.length:
            raise IndexError("Index out of range")
        newNode = {
            "value": value,
            "next_value": None
        }

        leader = self.get_to_index(index - 1)
        newNode["next_value"] = leader["next_value"]
        leader["next_value"] = newNode
        self.length += 1

        if index == self.length - 1:
            self.tail = newNode
        return self

    def get_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node["next_value"]
            counter += 1
        return current_node

    def remove(self, index):
        if index >= self.length:
            raise IndexError("Index out of range")

        leader = self.get_to_index(index - 1)
        node_to_delete = leader["next_value"]
        leader["next_value"] = node_to_delete["next_value"]
        self.length -= 1
        return self.print_list()


muLinkedList = LinkedList(10)

muLinkedList.append(5)
muLinkedList.append(16)
muLinkedList.preaprend(1)
muLinkedList.preaprend(200)
muLinkedList.preaprend(84)
muLinkedList.insert(2, 2)
print(muLinkedList.print_list())
muLinkedList.remove(1)
print(muLinkedList.print_list())
