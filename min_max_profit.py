class Solution:
    def maximumProfit(self, prices):
        res=0
        for i in range(len(prices)):
            buy=prices[i]
            for j in range(i+1,len(prices)):
                sell=prices[j]
                res=max(res,sell-buy)
        return res
