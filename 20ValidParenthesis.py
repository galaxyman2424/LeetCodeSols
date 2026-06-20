class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == ")" :
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
                    continue
            
            if char == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
                    continue

            if char == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
                    continue


            stack.append(char)

        return len(stack) == 0
