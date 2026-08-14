class Solution(object):
    def maxProfit(self, prices):
        minP = prices[0]; maxP = 0

        for i in range(1, len(prices)):
            if prices[i] - minP > maxP:
                maxP = prices[i] - minP
            else:
                if prices[i] < minP:
                    minP = prices[i]
                    
        return maxP
