class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        
        ans = []
        for i in range(0, len(strs)):
            if tuple(sorted(list(strs[i]))) not in strs_dict:
                strs_dict[tuple(sorted(list(strs[i])))] = len(ans)
                ans.append([strs[i]])

            elif tuple(sorted(list(strs[i]))) in strs_dict:
                print(strs_dict.get(tuple(sorted(list(strs[i])))))
                ans[strs_dict.get(tuple(sorted(list(strs[i]))))].append(strs[i])
        return list(ans)
