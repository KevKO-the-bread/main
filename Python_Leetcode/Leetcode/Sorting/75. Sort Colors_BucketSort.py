url=https://leetcode.com/problems/sort-colors/


class Solution(object):
    def sortColors(self, nums):
        count=[0,0,0]
        for n in nums:
            count[n]+=1
        i=0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i]=n
                i+=1
        return nums
