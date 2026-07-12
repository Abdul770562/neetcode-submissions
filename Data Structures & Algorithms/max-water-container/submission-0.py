class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l = 0
        r = n-1

        max_w = 0

        while(l<r):
            width = r-l
            height = min(heights[l], heights[r])
            max_w = max(max_w, width*height)

            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return max_w