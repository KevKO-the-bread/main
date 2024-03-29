url= https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution(object):
    def maxProfit(self, prices):
        l=0
        r=1
        maxP=0

        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP


class Solution(object):
    def maxProfit(self, prices):
        l,r=0,1
        profit=0

        while r<len(prices):
            if prices[l]<prices[r]:
                profit=profit+prices[r]-prices[l]
                l=r
            else:
                l=r
            r+=1
        return profit






