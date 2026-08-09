import numpy as np
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq=set(nums)
        if len(freq)<len(nums):
            return True
        else:
            return False
        