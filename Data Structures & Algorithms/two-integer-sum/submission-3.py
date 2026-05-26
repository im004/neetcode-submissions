class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            current = nums[i]
            complement = target - current

            if complement in seen:
                return [seen[complement], i]
            
            seen[nums[i]] = i


                        
        