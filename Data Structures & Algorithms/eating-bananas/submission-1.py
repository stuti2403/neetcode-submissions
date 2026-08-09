from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcu(piles: List[int], rate: int) ->int:
            hr=0
            for i in piles:
                hr = hr + ceil(i/rate)
            return hr
        piles.sort()
        max_bananas=piles[-1]
        l=0
        r=max_bananas-1
        mid=int((l+r+1)/2)
        k=max_bananas
        while l<=r:
            hours=calcu(piles, mid+1)
            if hours<=h and (mid+1)<=k:
                r=mid-1
                k=(mid+1)
            if hours>h:
                l=mid+1
            mid=int((l+r+1)/2)
        return k
        
        


        