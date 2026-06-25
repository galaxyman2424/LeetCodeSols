class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        first = nums[0]

        if first < nums[right] or right == 0:
            return first


        while left < right:
            mid = (left + right) // 2
            #print(nums[mid], left, mid, right)
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            
            #print(nums[mid], left, mid, right)

        return nums[left]