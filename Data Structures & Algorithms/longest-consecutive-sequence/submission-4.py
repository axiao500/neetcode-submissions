class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        longest = 1
        long_list = []
        if nums == []:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                longest += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                long_list.append(longest)
                longest = 1
        long_list.append(longest)
        return max(long_list)
        
        