class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s=[0]
        res=[0]*len(temperatures)
        if not temperatures:
            return s
        for idx in range(1,len(temperatures)):
            while s and temperatures[idx]>temperatures[s[-1]]:
                    x=s.pop()
                    print(x)
                    res[x]=(idx-x)
            s.append(idx)
        if s:
            for i in s:
                res[i]=0
        return res

            

            
        