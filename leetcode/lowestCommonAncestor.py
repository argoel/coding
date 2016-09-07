from essentialDS import *

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        aMap = {}
        self.mapAncestors(root, p, q, aMap)

        current = root

        while (aMap[current] == (True, True)):
            left = current.left
            right = current.right
            if aMap.get(left) == (True, True):
                current = left
            elif aMap.get(right) == (True, True):
                current = right
            else:
                return current

        return None

    def mapAncestors(self, root, p, q, ancestorMap = {}):
        pBool = False
        qBool = False

        if root == None:
            return (pBool, qBool)

        if root == p and root == q:
            pBool = True
            qBool = True
        elif root == p:
            pBool = True
        elif root == q:
            qBool = True

        left = root.left
        right = root.right

        lBoolPair = self.mapAncestors(left, p, q, ancestorMap)
        rBoolPair = self.mapAncestors(right, p, q, ancestorMap)

        print root.val
        print lBoolPair
        print rBoolPair

        pBool = pBool or lBoolPair[0] or rBoolPair[0]
        qBool = qBool or lBoolPair[1] or rBoolPair[1]
        
        print (pBool, qBool)

        ancestorMap[root] = (pBool, qBool)

        return (pBool, qBool)

    def isAncestorTest(self):
        l1 = [1,2]
        t = Tree(l1)
        root = t.getRoot()
        p = root
        q = root.left
        aMap = {}
        ans = self.mapAncestors(root, p, q, aMap)
        print "ans is {0}".format(ans)
        print "aMap is {0}".format(aMap)
        return aMap

