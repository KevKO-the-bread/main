url=https://leetcode.com/problems/subsets/description/

class Solution(object):
    def subsets(self, nums):

        res=[]

        subset=[]

        def dfs(i):
            if i>=len(nums):
                res.append(subset[:])
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)
        dfs(0)
