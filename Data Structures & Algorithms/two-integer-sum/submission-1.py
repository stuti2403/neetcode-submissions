import numpy as np
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i in range(len(nums)):
            if d[nums[i]]!=0:
                return [min(d[nums[i]]-1,i), max(d[nums[i]]-1,i)]
            diff=target-nums[i]
            d[diff]=i+1
            


