# Definition for a binary tree node.
# class TreeNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.insert(0,x)

    def pop(self):
        self.stack.pop(0)

    def top(self):
        return self.stack[0]

    def empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postorderList = []
        myStack = Stack()
        current = root
        while(current is not None):
            right = current.right
            if right is not None:
                myStack.push(right)
            myStack.push(current)
            current = current.left
            while(current is None and not(myStack.empty())):
                item = myStack.top()
                myStack.pop()
                ritem = item.right
                if not(myStack.empty()):
                    nitem = myStack.top()
                    if ritem == nitem:
                        myStack.pop()
                        myStack.push(item)
                        current = ritem
                    else:
                        postorderList.append(item.val)
                        current = None
                else:
                    postorderList.append(item.val)
                    current = None

        return postorderList
