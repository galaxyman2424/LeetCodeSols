class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:

            if num-1 not in num_set:
                curr = num
                curr_longest = 1
            else:
                continue
            
            while curr+1 in num_set:
                curr += 1
                curr_longest += 1


            longest = max(longest, curr_longest)
        
        return longest



        