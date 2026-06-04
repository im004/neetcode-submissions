class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        # Create frequency lists of size 26 (one for each lowercase letter)
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        # Populate the initial counts for s1 and the very first window of s2
        for i in range(len(s1)):
            # ord(char) - ord('a') converts letters 'a'-'z' to index integers 0-25
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
        # If the very first window is a perfect match, we are already done!
        if s1_counts == s2_counts:
            return True
            
        # Slide the window across the rest of s2
        # 'right' tracks the new character entering the window
        for right in range(len(s1), len(s2)):
            # 1. Add the new character entering the window on the right
            new_char_idx = ord(s2[right]) - ord('a')
            s2_counts[new_char_idx] += 1
            
            # 2. Identify and remove the old character falling out of the window on the left
            left_char_idx = ord(s2[right - len(s1)]) - ord('a')
            s2_counts[left_char_idx] -= 1
            
            # 3. Check if the updated window matches our target recipe
            if s1_counts == s2_counts:
                return True
                
        return False
        