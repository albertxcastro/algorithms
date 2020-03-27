class BinaryTree(object):

    def __init__(self, node):
        self.root = node
    
    def __str__(self):
        print('PreOrder:')
        self.root.printPreOrder()
        print('\nInOrder:')
        self.root.printInOrder()
        print('\nPostOrder:')
        self.root.printPostOrder()
        return ''


