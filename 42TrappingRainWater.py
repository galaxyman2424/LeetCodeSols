class Solution:
    def trap(self, height: List[int]) -> int:

        rain = 0

        left = 0
        lenlist = len(height) 

        while left != lenlist:
            if height[left] != 0:
                blocks = 0
                right = 0

                tallest = 0
                tallestindex = 0
                tallestblocks = 0

                for right in range(left + 1, lenlist):
                    #print(left, right, height[right], tallest)

                    if height[right] >= tallest:
                        #print(height[right], tallest)
                        tallest = height[right]
                        tallestindex = right
                        tallestblocks = blocks

                    if right == lenlist-1:
                        rain += (tallestindex-left-1) * min(height[left], height[tallestindex]) - tallestblocks
                        #print(rain, left, height[left], tallest, height[tallestindex], tallestblocks, 0)
                        left = tallestindex - 1
                        break

                    if height[right] >= height[left]:
                        rain += (right-left-1) * min(height[left], height[right]) - blocks
                        #print(rain, left, height[left], right, height[right], blocks)
                        left = right - 1
                        break
                    
                    blocks += height[right]
                
                left += 1
            else:
                left += 1
                continue

            



            
        return rain

