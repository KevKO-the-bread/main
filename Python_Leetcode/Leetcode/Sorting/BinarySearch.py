url=https://leetcode.com/problems/binary-search/

class Solution(object):
    def search(self, nums, target):
        L,R=0,len(nums)-1

        while L<=R:
            m=(L+R)//2

            if nums[m]>target:
                R=m-1
            elif nums[m]<target:
                L=m+1
            else:
                return m

        return -1
