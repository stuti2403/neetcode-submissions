class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        close2open={")":"(","]":"[","}":"{"}
        for c in s:
            if c in close2open:
                if st and st[-1]==close2open[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
                print(st)
        

        return True if not st else False

