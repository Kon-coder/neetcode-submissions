class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = []
        for val in s:
            if val.isalnum():
                clean.append(val.lower())
        return clean == clean[::-1]