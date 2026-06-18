class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        hash_table = {}
        i = 0

        for value in nums:
            if target-value not in hash_table:
                hash_table[value] = i
            else:
                return [hash_table[target-value], i]
            i+=1


