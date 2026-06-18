class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_table = {}
        i = 0

        for value in numbers:
            if target-value not in hash_table:
                hash_table[value] = i
            else:
                return [hash_table[target-value] + 1, i + 1]
            i+=1