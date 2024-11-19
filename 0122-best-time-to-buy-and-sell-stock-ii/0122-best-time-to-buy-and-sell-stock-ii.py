class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        #first day in the prices array
        buy_day = 0
        #second day in prices array
        sell_day = 1
        while sell_day < len(prices):
            profit = prices[sell_day] - prices[buy_day]
            #if there is profit
            if profit > 0:
                max_profit += profit
            #increment variables
            buy_day = sell_day
            sell_day+=1
        return max_profit

        
