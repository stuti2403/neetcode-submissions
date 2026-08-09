class Solution:
    def isPalindrome(self, s: str) -> bool:
        L=0
        R=len(s)-1
        while L<R:
            if not s[L].isalnum():
                L=L+1
                continue
            if not s[R].isalnum():
                R=R-1
                continue
            if L>R:
                return True
            if s[L].lower()==s[R].lower():
                L=L+1
                R=R-1
            else:
                return False
        return True
            
           
        