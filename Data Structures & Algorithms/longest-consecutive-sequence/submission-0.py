class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)
        
        check = set(nums)

        length = 0

        for num in check:
            if num-1 not in check:
                start = num
                curr_len = 1
                while start+1 in check:

                    start = start+1
                    curr_len = curr_len+1

                length = max(length, curr_len)

        return length