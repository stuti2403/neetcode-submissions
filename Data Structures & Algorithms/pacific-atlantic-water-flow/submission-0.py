from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n=len(heights),len(heights[0])
        p_que=deque()
        p_seen=set()

        a_que=deque()
        a_seen=set()

        for j in range(n):
            p_que.append((0,j))
            p_seen.add((0,j))

        for i in range(1,m):
            p_que.append((i,0))
            p_seen.add((i,0))

        for i in range(m):
            a_que.append((i,n-1))
            a_seen.add((i,n-1))

        for j in range(n-1):
            a_que.append((m-1,j))
            a_seen.add((m-1,j))
        

        def bfs(que,seen):
            while que:
                i,j=que.popleft()
                for i_offset,j_offset in [(0,1),(0,-1),(1,0),(-1,0)]:
                    r,c=i+i_offset,j+j_offset
                    if 0<=r<m and 0<=c<n and heights[r][c]>=heights[i][j] and (r,c) not in seen:
                        que.append((r,c))
                        seen.add((r,c))

            return seen

        p_set=bfs(p_que,p_seen)
        a_set=bfs(a_que,a_seen)
        return list(p_set.intersection(a_set))
        