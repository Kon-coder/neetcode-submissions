class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        
        for i in range(0, len(nums)):
            if nums[i]  not in num_dict:
                num_dict[nums[i]] = 1
            elif nums[i] in num_dict:
                num_dict[nums[i]] += 1
        
        return heapq.nlargest(k, num_dict, key=num_dict.get)