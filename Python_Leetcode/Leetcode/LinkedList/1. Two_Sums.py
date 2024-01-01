url= https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        prevMap={}
        for i in range(len(nums)):
            val=target-nums[i]
            if val in prevMap:
                return i, prevMap[val]
            prevMap[nums[i]]= i
