class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0

        diffs = [0]
        #i feel like this is a max subarry problem
        for i in range(1 ,len(prices)):
            diffs.append(prices[i] - prices[i-1])

        max_sum = diffs[0]
        current_sum = diffs[0]

        for num in diffs[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum



