class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        if not t or not s:
            return ""
        

        tcount = {}
        for c in t:
            tcount[c] = tcount.get(c, 0) + 1

        scount = {}
        left = 0
        

        have = 0
        need = len(tcount)
        res = [float("inf"), 0, 0] 
        

        for right in range(len(s)):
            char = s[right]
            scount[char] = scount.get(char, 0) + 1
            
            if char in tcount and scount[char] == tcount[char]:
                have += 1

            while have == need:
                window_size = right - left + 1
                if window_size < res[0]:
                    res = [window_size, left, right]
                
                left_char = s[left]
                scount[left_char] -= 1
                
                if left_char in tcount and scount[left_char] < tcount[left_char]:
                    have -= 1
                
                left += 1

        if res[0] == float("inf"):
            return ""
        
        return s[res[1]:res[2] + 1]
