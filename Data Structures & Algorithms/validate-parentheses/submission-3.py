class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i in ['[','{','(']:
                st.append(i)
            if i==']' and st!=[]:
                if st[-1]=='[':
                    st.pop()
                else:
                    return False
            elif i==']' and st==[]:
                return False
            if i=='}' and st!=[]:
                if st[-1]=='{':
                    st.pop()
                else:
                    return False
            elif i=='}' and st==[]:
                return False
            if i==')' and st!=[]:
                if st[-1]=='(':
                    st.pop()
                else:
                    return False
            elif i==')' and st==[]:
                return False
        if st==[]:
            return True
        else:
            return False
