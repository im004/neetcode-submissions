class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            current_temp = temperatures[i]
            
            # WHILE the stack isn't empty, AND today's temp is warmer than the day at the back of the line...
            while stack and current_temp > temperatures[stack[-1]]:
                # 1. Pop the waiting day's index off the stack
                prev_day_index = stack.pop()
                
                # 2. Calculate the difference between today (i) and that previous day
                res[prev_day_index] = i - prev_day_index
                
            # 3. Today joins the back of the line (push today's INDEX, not temperature)
            stack.append(i)
            
        return res