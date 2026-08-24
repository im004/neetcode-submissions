class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        cs = {}
        ct = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            cs[s[i]] = cs.get(s[i], 0) + 1
            ct[t[i]] = ct.get(t[i], 0) + 1
        
        return cs == ct


        
        