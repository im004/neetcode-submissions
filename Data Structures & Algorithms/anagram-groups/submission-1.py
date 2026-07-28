class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bins = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in bins:
                bins[sorted_word].append(word)
            
            else:
                bins[sorted_word] = [word]
        
        return list(bins.values())
            
        