class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker_s = {}
        tracker_t = {}
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            if s[i] not in tracker_s:
                tracker_s[s[i]] = 1
            elif s[i] in tracker_s:
                tracker_s[s[i]] += 1

            if t[i] not in tracker_t:
                tracker_t[t[i]] = 1
            elif t[i] in tracker_t:
                tracker_t[t[i]] += 1
            
                
        print(tracker_t)
        print(tracker_s)

        if tracker_s == tracker_t:
            return True
        else: 
            return False
    

