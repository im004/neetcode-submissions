class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Step 1: Count frequencies of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # Step 2: Sort the unique numbers by their frequency in descending order
        sorted_nums = sorted(count.keys(), key=count.get, reverse=True)
        
        # Step 3: Return the first 'k' elements from the sorted list
        return sorted_nums[:k]

        