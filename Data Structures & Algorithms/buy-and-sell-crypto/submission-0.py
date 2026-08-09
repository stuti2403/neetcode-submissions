class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        maxi=0
        for i in range(0,l-1):
            for j in range(i+1,l):
                if prices[j]>prices[i]:
                    print("in if")
                    print(prices[j])
                    pr=prices[j]-prices[i]
                    if pr>maxi:
                        maxi=pr
        return maxi
