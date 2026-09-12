class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list)
        for i,j in prerequisites:
            g[i].append(j)
        UNVISITED=0
        VISITING=1
        TAKE=2
        states=[UNVISITED] * numCourses

        def dfs(node):
            state=states[node]
            if state==TAKE: return True
            elif state==VISITING: return False
            states[node]=VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node]=TAKE
            return True 
        
        for node in range(numCourses):
            if not dfs(node): return False

        return True
        