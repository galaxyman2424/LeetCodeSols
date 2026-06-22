class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        stack = []

        for temp in range(len(temperatures)):        
            while stack and temperatures[temp] > temperatures[stack[-1]]:
                i = stack.pop()
                ans[i] = temp - i
            stack.append(temp)
                
                    
        
        return ans






class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = []
        stack = []

        listlen = len(temperatures)

        for temp in range(0, listlen):
            ans.append(0)
            stack.append(temp)
            for i in range(len(stack)-1, -1, -1):

                if temperatures[stack[i]] < temperatures[temp]:
                    ans[stack[i]] = temp - stack[i]
                    stack.pop(i)
                    
        
        return ans

