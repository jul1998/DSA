# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
#     def get_level(self):
#         level = 0
#         parent = self.parent
#         while parent:
#             level += 1
#             parent = parent.parent
#         return level
#
#
#     def print_tree(self):
#         spaces = " " * self.get_level() * 3
#         print(spaces + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()
#
#
#
#
# def build_product_tree():
#     root = TreeNode("Electronics")
#
#     laptop = TreeNode("Laptop")
#     laptop.add_child(TreeNode("Mac"))
#     laptop.add_child(TreeNode("Surface"))
#     laptop.add_child(TreeNode("Thinkpad"))
#
#     cellphone = TreeNode("Cell Phone")
#     cellphone.add_child(TreeNode("iPhone"))
#     cellphone.add_child(TreeNode("Google Pixel"))
#     cellphone.add_child(TreeNode("Vivo"))
#
#     tv = TreeNode("TV")
#     tv.add_child(TreeNode("Samsung"))
#     tv.add_child(TreeNode("LG"))
#
#     root.add_child(laptop)
#     root.add_child(cellphone)
#     root.add_child(tv)
#
#     return root
#
# if __name__ == '__main__':
#     root = build_product_tree()
#     root.print_tree()

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return

        itr = self.root
        while True:
            if data < itr.data:
                if not itr.left:
                    itr.left = node
                    break
                else:
                    itr = itr.left
            else:
                    #Rigth
                if not itr.right:
                    itr.right = node
                    break
                else:
                    itr = itr.right

    def lookup(self,value):
        itr = self.root
        while itr:
            if value > itr.data:
                if value == itr.data:
                    return True
                else:
                   itr = itr.right
            else:
                if value == itr.data:
                    return True
                else:
                    itr = itr.left
        return False

    def remove(self, value):
        itr = self.root
        while itr:
            if value >= itr.data:
                if value == itr.data:
                    itr.data = itr.right
                    return True
                else:
                    itr = itr.right
            else:
                if value == itr.data:
                    itr.data = itr.left
                else:
                    itr = itr.left
        return False

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(170)
tree.insert(1)
tree.insert(6)
print(tree.lookup(170))
print(tree.remove(20))
print(tree.remove(1))
print(tree.insert(6))
# tree.insert(9)