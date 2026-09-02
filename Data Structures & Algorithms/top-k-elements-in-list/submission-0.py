class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        #creates [[]]
        for i in range(len(nums) + 1):
            freq.append([])

        #iterates through the list and creates a frequency dict
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        #appends the dict to the list
        for n,c in count.items(): 
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result
        