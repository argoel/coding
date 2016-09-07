class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.insert(0,x)
    def pop(self):
        self.stack.pop()
    def top(self):
        return self.stack[0]
    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class Queue(object):
    def __init__(self):
        self.queue = []
    def enqueue(self, x):
        self.queue.append(x)
    def dequeue(self):
        return self.queue.pop(0)
    def empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = TreeNode()

    def __init__(self, tList):
        self.root = TreeNode()
        Q = Queue()
        Q.enqueue(self.root)

        for i in range(len(tList)):
            current = Q.dequeue()
            val = tList[i]
            if (val == "null"):
                continue
            else:
                current.val = val
                lNode = TreeNode()
                rNode = TreeNode()
                current.left = lNode
                current.right = rNode
                Q.enqueue(lNode)
                Q.enqueue(rNode)

    def getRoot(self):
        return self.root
