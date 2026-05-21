class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start by assuming the minimum price is the very first day's price
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # 1. If the current price is CHEAPER than our min_price, 
            #    update min_price to be this current price.
            if price < min_price:
                min_price = price
            
            # 2. Otherwise, see how much profit we'd make selling today.
            #    If that profit is bigger than our max_profit, update max_profit!
            else:
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
                    
        return max_profit