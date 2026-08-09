from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)

        for i in strs:
            perword={}
            for j in i:
                perword[j]=1+perword.get(j,0)
            hashable_perword=frozenset(perword.items())
            d[hashable_perword].append(i)

        print(d)
        res=[]
        for i,j in d.items():
            res.append(j)
        return res 

