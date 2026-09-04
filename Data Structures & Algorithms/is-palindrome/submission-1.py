class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(char for char in s if char.isalnum())
        palindrome = ""
        for i in range(-1, -(len(word) + 1), -1):
            palindrome = palindrome + word[i]

        print(palindrome)
        print(word)
        if palindrome.lower() == word.lower():
            return True

        return False