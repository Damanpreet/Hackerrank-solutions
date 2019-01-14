from test import testEqual

def BinaryTree(r):
    return [r,[],[]]

def addLeftNode(root, val):
    ele = root.pop(1)
    if len(ele) > 1:
        root.insert(1, [val, ele, []])
    else:
        root.insert(1, [val, [], []])
    return root

def addRightNode(root, val):
    ele = root.pop(2)
    if len(ele) > 1:
        root.insert(2, [val, [], ele])
    else:
        root.insert(2, [val, [], []])
    return root

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

def getRootVal(root):
    return root[0]

def buildTree():
    r = BinaryTree('a')
    addLeftNode(r, 'b')
    addRightNode(r, 'e')
    addRightNode(r, 'c')
    t = getLeftChild(r)
    addRightNode(t, 'd')
    t = getRightChild(r)
    addRightNode(t, 'f')
    return r

ttree = buildTree()
testEqual(getRootVal(getRightChild(ttree)),'c')
testEqual(getRootVal(getRightChild(getLeftChild(ttree))),'d')
testEqual(getRootVal(getRightChild(getRightChild(ttree))),'f')
