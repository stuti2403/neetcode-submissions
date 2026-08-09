class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=s.replace(' ','')
        print(st)
        i=0
        j=len(st)-1
        while i<j:
            ii=st[i]
            jj=st[j]
            if not ii.isalpha() and not ii.isdigit():
                print("i is ")
                print(i)
                print("j is")
                print(j)
                print("ii is not alpha")
                i=i+1
            if not jj.isalpha() and not jj.isdigit():
                j=j-1
            if i>j:
                return True
            else:
                if st[i].lower()==st[j].lower():
                    i=i+1
                    j=j-1
                else:
                    return False
        return True
            
           
        