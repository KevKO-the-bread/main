url=https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution(object):
    def twoSum(self, numbers, target):
        if not numbers:
            return
        
        l=0

        r=len(numbers)-1

        while l<r:
            summe=numbers[l]+numbers[r]
            if summe>target:
                r-=1
            elif summe<target:
                l+=1
            else: 
                return l+1, r+1
