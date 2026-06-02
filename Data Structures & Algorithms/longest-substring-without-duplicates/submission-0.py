class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0
        
        # 'right' acts as the leader, stepping through the string character by character
        for right in range(len(s)):
            
            # WHILE the character at 'right' is a duplicate (already in our set)...
            # We are in trouble. We must shrink the window from the left!
            while s[right] in seen:
                # 1. Remove the character at 'left' from our checklist
                seen.remove(s[left])
                # 2. Move the 'left' pointer forward by 1
                left += 1
            
            # Now the runway is clear! 
            # 3. Add the character at 'right' to our checklist
            seen.add(s[right])
            
            # 4. Calculate the current window size: (right - left + 1)
            curr_size = right - left + 1
            # 5. Update 'max_len' if this window is a new record
            max_len = max(max_len, curr_size)
            
        return max_len
        
            
        