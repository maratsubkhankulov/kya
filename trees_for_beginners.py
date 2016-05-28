from collections import deque

class Node:
    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data

def createTree():
    # Create tree
    tree = Node("a", Node("b", None, None), Node("c", None, None))

    # Insert nodes
    tree.left.left = Node("d", None, None)
    tree.left.right = Node("e", None, None)
    tree.right.left = Node("f", None, None)
    tree.right.right = Node("g", None, None)

    return tree

def inOrder(node):
    if node:
        # Go left
        inOrder(node.left)
        # Visit
        print(node.data)
        # Go right
        inOrder(node.right)

def preOrder(node):
    if node:
        # Visit
        print(node.data)
        # Go left
        preOrder(node.left)
        # Go right
        preOrder(node.right)

def postOrder(node):
    if node:
        # Go left
        postOrder(node.left)
        # Go right
        postOrder(node.right)
        # Visit
        print(node.data)

def levelOrder(tree):
    if not tree:
        print("root is null")
        return
    queue = deque()
    queue.append(tree)
    while len(queue) > 0:
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print(node.data)

def treeHeight(node, depth):
    if node:
        # Go left
        leftHeight = treeHeight(node.left, depth + 1)
        # Go right
        rightHeight = treeHeight(node.right, depth + 1)
        return max(leftHeight, rightHeight)
    else:
        return depth

def numLeaves(node, count):
    if node:
        # Go left
        count = numLeaves(node.left, count)
        # Go right
        count = numLeaves(node.right, count)
        if node.left == None and node.right == None:
            count += 1
    return count

def preOrderPrint(node, depth):
    if node:
        # Visit
        print(' '*4*depth + node.data)
        # Go left
        preOrderPrint(node.left, depth + 1)
        # Go right
        preOrderPrint(node.right, depth + 1)

def binaryInsert(bst, value):
    print("implement me")
    return

def test():
    tree = createTree()
    print("inOrder")
    inOrder(tree)
    print("preOrder")
    preOrder(tree)
    print("postOrder")
    postOrder(tree)
    print("levelOrder")
    levelOrder(tree)

    print("height")
    print(treeHeight(tree, 0))

    print("num leaves", numLeaves(tree, 0), numLeaves(tree, 0) == 4)

    preOrderPrint(tree,0)
