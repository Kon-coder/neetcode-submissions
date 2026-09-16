class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False 
        count1 = {} 
        count2 = {} 
        # Count characters in s1 
        for c in s1: 
            count1[c] = 1 + count1.get(c, 0) 
        # Create the first window 
        for c in s2[:len(s1)]: 
            count2[c] = 1 + count2.get(c, 0) 
            
        # Check the first window 
        if count1 == count2: 
            return True 
            
        left = 0 
            
        # Slide the window 
            
        for right in range(len(s1), len(s2)): 
            # Add the new character 
            count2[s2[right]] = 1 + count2.get(s2[right], 0) 
                
            # Remove the character leaving the window 
            count2[s2[left]] -= 1
            # Remove key if its count reaches 0 
            if count2[s2[left]] == 0: 
                del count2[s2[left]] 
            left += 1 
            # Compare the current window with s1 
            if count1 == count2: 
                return True 
            
        return False