class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][1] > h:
                popindex, popheight = stack.pop()

                width = i - popindex
                max_area = max(max_area, popheight*width)
                start = popindex

            stack.append((start,h))
        
        for i,h in stack:
            width = len(heights) - i
            max_area = max(max_area, width*h)
        
        return max_area
