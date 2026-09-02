class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for number, c in count.items():
            freq[c].append(number)
        result = []
        for n in range(len(freq) - 1, 0, -1):
            for i in freq[n]:
                result.append(i)
                if len(result) == k:
                    return result

        