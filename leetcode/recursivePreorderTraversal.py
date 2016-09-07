# Definition for a binary tree node.
# class TreeNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        left = root.left
        right = root.right
        preorderList = [root.val]
        if left is not None:
            leftTraversal = self.preorderTraversal(left)
            preorderList.extend(leftTraversal)
        if right is not None:
            rightTraversal = self.preorderTraversal(right)
            preorderList.extend(rightTraversal)
        return preorderList
