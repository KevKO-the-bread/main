url=https://leetcode.com/problems/search-in-a-binary-search-tree/description/

class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None

        if root.val<val:
            return self.searchBST(root.right, val)
        elif root.val>val:
            return self.searchBST(root.left, val)
        else:
            return root
