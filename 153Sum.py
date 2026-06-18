class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        sols = set()

        for i,num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            seen = set()

            for j in range(i+1, len(nums)):
                complement = -nums[i]-nums[j]
                if complement in seen:
                    if (nums[i], complement, nums[j]) not in sols:
                        result.append([nums[i], complement, nums[j]])
                        sols.add((nums[i], complement, nums[j]))
                seen.add(nums[j])
            
        return result
