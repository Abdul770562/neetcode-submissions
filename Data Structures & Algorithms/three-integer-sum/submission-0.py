class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums = sorted(nums)

        elem = 0
        result = [] 

        for elem in range(n):
            if elem > 0 and nums[elem] == nums[elem-1]:
                continue

            new_target = -nums[elem]

            l = elem + 1
            r = len(nums) - 1

            while(l<r):
                s = nums[l] + nums[r]

                if s == new_target:
                    result.append([nums[l],nums[r],nums[elem]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1     
                    while l < r and nums[r] == nums[r+1]:
                        r-= 1    
                elif s > new_target:
                    r-=1
                else:
                    l+=1 

        return result


