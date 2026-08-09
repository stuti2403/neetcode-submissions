class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        oper=['+','-','*','/']
        for i in tokens:
            if i in oper:
                a_r=s.pop()
                a_l=s.pop()
                if i == '+':
                    res=a_l + a_r
                if i == '-':
                    res=a_l - a_r
                if i == '*':
                    res=a_l * a_r
                if i == '/':
                    res=int(a_l/a_r)
                s.append(res)
            else:
                s.append(int(i))
        return s[0]
                


        