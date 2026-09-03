class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        results = [1] * len(nums)
        for i in range(len(nums)):
            results[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums) -1 , -1 , -1): 
            results[i] = results[i] * postfix
            postfix = postfix * nums[i]

        return results
        