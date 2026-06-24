class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        posspeed = []

        for i in range (len(position)):
            posspeed.append((position[i], speed[i]))
        
        posspeed = sorted(posspeed, reverse=True)

        stack = []

        for pos, speed in posspeed:

            time = float((target-pos)/speed)

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        
        return len(stack)



        