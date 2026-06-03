class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}  
        left = 0
        max_len = 0
        max_count = 0  
        
        for right in range(len(s)):
            # Update the count of the current character
            counts[s[right]] = counts.get(s[right], 0) + 1
            
            # Keep track of the highest frequency seen in the current window
            max_count = max(max_count, counts[s[right]])
            
            # Calculate current window size: (right - left + 1)
            
            
            # THE CONFLICT: If imposters (window_size - max_count) exceed k...
            while (right - left + 1) - max_count > k:
                # Shrink from the left
                counts[s[left]] -= 1
                left += 1
            
            # Record the maximum length of a valid window found so far
            # Re-calculate window_size here because left might have moved!
            max_len = max(max_len, right - left + 1)
            
        return max_len
        