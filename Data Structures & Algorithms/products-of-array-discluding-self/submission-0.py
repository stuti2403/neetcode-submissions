import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[int(0)]*len(nums)
        zeros_ind=[]
        pr=1
        n_new=[]
        for i,n in enumerate(nums):
            if n==0:
                zeros_ind.append(i)
            else:
                n_new.append(n)
            pr=pr*n
        print(pr)
        if pr!=0:
            for i,n in enumerate(nums):
                output[i]=int(pr/n)
        else:
            if len(zeros_ind)==1:
                pr_new=1
                for i in n_new:
                    pr_new=pr_new*i
                output[zeros_ind[0]]=pr_new             
        return output


                