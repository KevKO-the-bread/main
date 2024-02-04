url=https://leetcode.com/problems/delete-node-in-a-bst/

class Solution(object):
    def minVal(self,root):
        cur=root
        while cur and cur.left:
            cur=cur.left
        return cur

    def deleteNode(self, root, val):
        if not root:
            return None
        
        if root.val>val:
            root.left=self.deleteNode(root.left, val)

        elif root.val<val:
            root.right=self.deleteNode(root.right, val)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minVal=self.minVal(root.right)
                root.val=minVal.val
                root.right=self.deleteNode(root.right, minVal.val)
        return root
