class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0 
        L = 0
        charset = {}
        for i in range(len(s)):
            if s[i] in charset:
                L = max(L, charset[s[i]] + 1)

            charset[s[i]] = i

            ans = max(ans, i - L + 1)

        return ans
            

            