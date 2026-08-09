class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        l=len(heights)-1
        water=0
        while l>=1:
            ar=l*min(heights[i],heights[j])   
            if ar>water:
                water=ar
            l=l-1
            if heights[i]<heights[j]:
                i=i+1
            elif heights[j]<heights[i]:
                j=j-1
            else:
                i=i+1
                j=j-1
                l=l-1

        return water