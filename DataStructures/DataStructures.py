from Structures.Tree.BinaryTree import BinaryTree
from Structures.Tree.Node import Node

nodevals = [11, 6, 8, 19, 4, 10, 5, 17, 43, 49, 31]
root = Node(nodevals[0])
btree = BinaryTree(root)

nodevals.pop(0)

for i in nodevals:
    node = Node(i)
    btree.root.insert(node)

print(str(btree))

anotherNode = btree.root.findNode(11) #43 has childs 31 and 49
print(str(anotherNode))
