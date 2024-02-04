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

iterative:
def inorderTraversal(self, root):
    res = []
    stack = []
    cur = root
    
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)  # Änderung: Fügen Sie den Wert von cur zur Ergebnisliste hinzu, nicht cur selbst
        cur = cur.right

    return res  # Änderung: Rückgabe der Ergebnisliste, nicht von cur




def preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)
