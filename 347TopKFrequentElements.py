class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        for num in freq:
            count = freq[num]
            buckets[count].append(num)

        result = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result

