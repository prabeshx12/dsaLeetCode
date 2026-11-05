# Tree Traversal Methods and their implementation
class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Simple Tree
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.left = node2
node1.right = node3

def preOrder(node):
    if node:
        print(node.value, end=" ")
        preOrder(node.left)
        preOrder(node.right)

def inOrder(node):
    if node:
        inOrder(node.left)
        print(node.value, end=" ")
        inOrder(node.right)

def postOrder(node):
    if node:
        postOrder(node.left)
        postOrder(node.right)
        print(node.value, end=" ")


# Example
preOrder(node1)
print()
inOrder(node1)
print()
postOrder(node1)
