class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        left = 0
        right = len(height) - 1
        
        max_left = height[left]
        max_right = height[right]
        total_water = 0
        
        while left < right:
            # If the left boundary is shorter, it limits the water level
            if max_left < max_right:
                left += 1
                # Update the tallest wall seen on the left
                max_left = max(max_left, height[left])
                # Add the trapped water at this slot to our total
                total_water += max_left - height[left]
            else:
                # If the right boundary is shorter or equal, it limits the water level
                right -= 1
                # Update the tallest wall seen on the right
                max_right = max(max_right, height[right])
                # Add the trapped water at this slot to our total
                total_water += max_right - height[right]
                
        return total_water