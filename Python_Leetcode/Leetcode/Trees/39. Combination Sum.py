url= https://leetcode.com/problems/combination-sum/description/

class Solution(object):
    def combinationSum(self, candidates, target):

        res=[]
        sub=[]

        def dfs(i, currSum):
            if currSum==target:
                res.append(sub[:])
                return

            if i>=len(candidates) or currSum>target:
                return
            
            sub.append(candidates[i])
            dfs(i, currSum+candidates[i])

            sub.pop()
            dfs(i+1, currSum)

        dfs(0,0)  
        return res  
