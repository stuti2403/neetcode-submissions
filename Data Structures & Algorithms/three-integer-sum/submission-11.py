class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for ind,x in enumerate(nums):
            print("in f")
            if x>0: 
                break
            if x==nums[ind-1] and ind!=0:
                continue
            target=(-1)*x
            print("target")
            print(target)
            i=ind+1
            j=len(nums)-1
            while i<j:
                s=nums[i]+nums[j]
                if s==target:
                    res.append([x,nums[i],nums[j]])
                    i=i+1
                    j=j-1
                    while nums[i]==nums[i-1] and i<j:
                        i=i+1
                if s<target:
                    i=i+1
                if s>target:
                    j=j-1
        return res