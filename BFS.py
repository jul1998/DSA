class BinarySearchTree:
    def __init__(self):
        self.root = None

    def breathFirstSearch(self):
        current_node = self.root
        myList = []
        myQ = []

        myQ.append(current_node)

        while len(myQ)> 0:
            current_node = myQ.pop(0)
            print(current_node.value)
            myList.append(current_node.value)
            if current_node.left:
                myQ.append(current_node.left)
            if current_node.right:
                myQ.append(current_node.right)