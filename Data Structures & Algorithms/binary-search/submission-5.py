class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid=int((l+r+1)/2)
        if mid==0:
            return mid if nums[mid]==target else -1
        while l<r:
            print(l,r, mid)
            if nums[mid]==target:
                return mid
            if nums[l]==target:
                return l
            if nums[r]==target:
                return r
            mid=int((l+r+1)/2)
            if nums[mid] > target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
        return -1

        
        