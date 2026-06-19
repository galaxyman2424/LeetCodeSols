class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0
        
        i = 0
        j = len(height) - 1

        while i!=j:
            if min(height[i], height[j])*(j-i) > maxvol:
                maxvol = min(height[i], height[j])*(j-i)


            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return maxvol

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0
        lenlist = len(height)

        for i,num in enumerate(height):
            for j in range(i, lenlist):

                if height[i]*(lenlist-i) < maxvol:
                    continue

                if (j-i)*min(height[i], height[j]) > maxvol:
                    maxvol = (j-i)*min(height[i], height[j])

        return max