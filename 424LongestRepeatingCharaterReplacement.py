class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        ans = 0
        left = 0
        count = {}
        max_freq = 0

        for right in range(len(s)):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1
            
            max_freq = max(max_freq, count[s[right]])

            if right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1) 

            
        
        return ans