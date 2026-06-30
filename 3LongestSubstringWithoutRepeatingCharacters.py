class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        left = 0
        right = 0
        last_seen = {}

        while right < len(s):
            if s[right] in last_seen:
                if last_seen[s[right]] >= left:
                    left = last_seen[s[right]] + 1

            if right - left + 1 > ans:
                ans = right-left+1

            last_seen[s[right]] = right
            right += 1

        return ans