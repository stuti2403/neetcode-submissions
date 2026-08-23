from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        non_dupe=set(s)
        n="".join(a for a in non_dupe)
        if s==non_dupe or s=="":
            return 0
        else:
            max_l=0
            l=0
            r=0
            hash_map={i:-1 for i in s}
            while r<=len(s)-1:
                if hash_map[s[r]]!=-1:
                    if hash_map[s[r]]>=l:
                        l=hash_map[s[r]]+1
                hash_map[s[r]]=r
                length=r-l+1
                max_l=max(max_l,length)
                r=r+1
            return max_l
                    

                

        
        