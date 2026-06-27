class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        result = right

        while left <= right:
            mid = (left + right)//2

            tot_hours = 0
            for pile in piles:
                tot_hours += math.ceil(pile/mid)

            if tot_hours <= h:
                result = mid

                right = mid - 1 
            else:
                left = mid + 1

        return result

