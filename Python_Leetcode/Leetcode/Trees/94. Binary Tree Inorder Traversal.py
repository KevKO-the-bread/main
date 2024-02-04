url=https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution(object):
    def __init__(self):
        self.root_list = []
    def inorderTraversal(self, root):
        if not root:
            return None

        self.inorderTraversal(root.left)
        self.root_list.append(root.val)
        self.inorderTraversal(root.right)

        return self.root_list
