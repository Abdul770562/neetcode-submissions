class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        freq = {}

        for elem in nums:
            freq[elem] = freq.get(elem,0) + 1

        bucket = [[] for _ in range(n+1)]

        for num,count in freq.items():
            bucket[count].append(num)

        m = len(bucket)

        result = []

        for i in range(m-1, 0, -1):

            for num in bucket[i]:

                result.append(num)

                if len(result) == k:
                    return result