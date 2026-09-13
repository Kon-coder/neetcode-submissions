class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        max_freq = 0
        charset = {}
        L = 0
        for right in range(len(s)):
            charset[s[right]] = charset.get(s[right], 0) + 1

            max_freq = max(max_freq, charset[s[right]])

            window_size = right - L + 1
            changes_needed = window_size - max_freq

            while changes_needed > k:
                charset[s[L]] -= 1
                L += 1

                window_size = right - L + 1
                changes_needed = window_size - max_freq

            longest = max(longest, right - L + 1)

        return longest


