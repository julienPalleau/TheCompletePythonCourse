from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

# print(tree.head)
# print(tree.head.left)
# print(tree.head.right)

# print("In Order")
# tree.inorder()
# print("\n")
# print("In pre-Oroder")
# tree.preorder()
print(tree.find(11))
