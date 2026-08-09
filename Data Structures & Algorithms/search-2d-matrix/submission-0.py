class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #flatten it
        # nums=[item for sublist in matrix for item in sublist]
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=(m*n)-1
        mid_linear=int((l+1+r)/2)
        mid_l=int(mid_linear/n)
        mid_r=mid_linear%n
        while l<=r:
            if matrix[mid_l][mid_r]==target:
                return True
            mid_linear=int((l+1+r)/2)
            mid_l=int(mid_linear/n)
            mid_r=mid_linear%n
            if matrix[mid_l][mid_r]>target:
                r=mid_linear-1
            if matrix[mid_l][mid_r]<target:
                l=mid_linear+1
        return False
        