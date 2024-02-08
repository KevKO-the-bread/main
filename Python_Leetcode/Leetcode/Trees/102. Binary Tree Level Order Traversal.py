url=https://leetcode.com/problems/binary-tree-right-side-view/

class Solution(object):
    def levelOrder(self, root):
        queue=deque()
    
        if root:
            queue.append(root)
        
        res=[]
        while len(queue)>0:
            level=[]
        
            for i in range(len(queue)):
                curr=queue.popleft()
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(level)
