url=https://leetcode.com/problems/koko-eating-bananas/

class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            if hours <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res
