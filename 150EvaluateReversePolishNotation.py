class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        copystack = []
        cstacklen = 0

        for tok in tokens:
            
            if tok == "*":
                copystack[cstacklen-2] = copystack[cstacklen-2] * copystack[cstacklen-1]
                copystack.pop()
                cstacklen -= 1
            elif tok == "+":
                copystack[cstacklen-2] = copystack[cstacklen-2] + copystack[cstacklen-1]
                copystack.pop()
                cstacklen -= 1
            elif tok == "-":
                copystack[cstacklen-2] = copystack[cstacklen-2] - copystack[cstacklen-1]
                copystack.pop()
                cstacklen -= 1
            elif tok == "/":
                copystack[cstacklen-2] = int(copystack[cstacklen-2] / copystack[cstacklen-1])
                copystack.pop()
                cstacklen -= 1
            else: 
                copystack.append(int(tok))
                cstacklen += 1
        
        return copystack[0]
            
