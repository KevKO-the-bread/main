url= https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if root.val<val:
            root.right= self.insertIntoBST(root.right, val)
        elif root.val>val:
            root.left= self.insertIntoBST(root.left, val)
        return root
