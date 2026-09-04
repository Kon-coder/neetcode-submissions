class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_set = set(nums)
        maxi = 0
        ans = 0
        for current in unique_set: 
            if current - 1 not in unique_set: 
                ans = 0 
                while current in unique_set: 
                    ans += 1 
                    current += 1 
            
            maxi = max(maxi, ans) 
    
        return maxi