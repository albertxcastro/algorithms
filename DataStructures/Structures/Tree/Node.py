class Node(object):
    """Represents a node in a tree"""
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def insert(self, node):
        if node.data < self.data:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)
        elif node.data > self.data:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)

    def printPreOrder(self):
        print(self.data, end = ' ')
        if self.left is not None:
            self.left.printPreOrder()
        if self.right is not None:
            self.right.printPreOrder()

    def printInOrder(self):
        if self.left is not None:
            self.left.printInOrder()
        print(self.data, end = ' ')
        if self.right is not None:
            self.right.printInOrder()

    def printPostOrder(self):
        if self.left is not None:
            self.left.printPostOrder()
        if self.right is not None:
            self.right.printPostOrder()
        print(self.data, end = ' ')

    def findNode(self, value, level = 0):
        if value == self.data:
            return self
        elif self.left is not None and value < self.data:
            return self.left.findNode(value)
        elif self.right is not None and value > self.data:
            return self.right.findNode(value)
        else:
            return None


    def __str__(self):
        return f'Data: {self.data}, L: {self.left}, R: {self.right}\n'