class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        


        #find pivot point
        mid = 0
        while left < right:
            if nums[left] < nums[right]:
                break
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid


        newleft = 0
        newright = len(nums) - 1
        if nums[newleft] > nums[newright]:
            if target < nums[newleft]:
                newleft = mid + 1
            else:
                newright = mid


        
        while newleft <= newright:
            newmid = (newright + newleft) // 2

            if nums[newmid] == target:
                return newmid
            elif nums[newmid] > target:
                newright = newmid - 1
            elif nums[newmid] < target:
                newleft = newmid + 1
            
        
        return -1