import numpy as np 
from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd=defaultdict(int)
        td=defaultdict(int)
        if len(s)!=len(t):
            return False
        else:
            sset=set(s)
            tset=set(t)
            if sset!=tset:
                return False
            else: 
                for i in s:
                    sd[i]+=1
                for j in t:
                    td[j]+=1
                if sd==td:
                    return True
                else:
                    return False