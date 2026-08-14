class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]; maxProf = 0

        for i in range(1, len(prices)):
            if prices[i] - minPrice > maxProf:
                maxProf = prices[i] - minPrice
            else:
                if prices[i] < minPrice:
                    minPrice = prices[i]
                    
        return maxProf
