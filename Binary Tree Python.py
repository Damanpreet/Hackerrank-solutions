from test import testEqual

class BinaryTree:
    def __init__(self, val):
        self.root = val
        self.LeftChild = None
        self.RightChild = None
        
    def getRightChild(self):
        return self.RightChild

    def getLeftChild(self):
        return self.LeftChild

    def setLeftChild(self, val):
        if self.LeftChild == None:
            self.LeftChild = BinaryTree(val)
        else:
            branch = BinaryTree(val)
            branch.LeftChild = self.LeftChild
            self.LeftChild = branch
    
    def setRightChild(self, val):
        if self.RightChild == None:
            self.RightChild = BinaryTree(val)
        else:
            branch = BinaryTree(val)
            branch.RightChild = self.RightChild
            self.RightChild = branch
    
    def getRootVal(self):
        return self.root
    
def buildTree():
    t = BinaryTree('a')
    t.setLeftChild('b')
    t.setRightChild('c')
    node = t.getLeftChild()
    node.setRightChild('d')
    node = t.getRightChild()
    node.setLeftChild('e')
    node.setRightChild('f')
    return t
    
ttree = buildTree()

testEqual(ttree.getRightChild().getRootVal(),'c')
testEqual(ttree.getLeftChild().getRightChild().getRootVal(),'d')
testEqual(ttree.getRightChild().getLeftChild().getRootVal(),'e')
