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

        return maxvol