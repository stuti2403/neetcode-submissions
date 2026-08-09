class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L=0
        R=len(numbers)-1
        while R>=0:
            if numbers[L]+numbers[R]==target:
                return [L+1,R+1]
            if numbers[L]+numbers[R]<target:
                L=L+1
            if numbers[L]+numbers[R]>target:
                R=R-1
        
        