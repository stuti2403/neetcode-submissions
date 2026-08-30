class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        print(m,n)
        maxarea=0
        def dfs(i,j, area:int):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return area
            grid[i][j]=0
            area = area +1
            area=dfs(i,j+1,area)
            area=dfs(i+1,j,area)
            area=dfs(i,j-1,area)
            area=dfs(i-1,j,area)
            # print("inside")
            # print(area)
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    # print(i,j)
                    area=dfs(i,j,1)-1
                    if area>maxarea:
                        maxarea=area
        return maxarea


