class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        maxi=0
        for win_s in range(1,l):
            i=0
            i_max=l-win_s
            while(i<i_max):
                j=i+win_s
                pr=prices[j]-prices[i]
                if pr>maxi:
                    maxi=pr
                i=i+1
        return maxi
