#array having the range of buy and sell rates

class Solution:
    def maxProfit(self, prices) -> int:
        max_prof=0
        buy_at=prices[0] #considered first element of array is where stock is bought
        for i in range(1,len(prices)):

            if prices[i]<buy_at:
                #if the second element, or element ahead is smalleer than buy_at
                # print("enter if")
                #then buy_at is changed to that element
                buy_at=prices[i]
            #buy_at and sell_at are series of things, then traversal is happening
            # max_prof is when i have bought at smallest, and sold at largest    
            max_prof=max(max_prof,(prices[i]-buy_at))
            # print("max_prof",max_prof)
        if max_prof<=0: #if profit is minus or zero
           return 0
        else:
            return max_prof

sol=Solution()
print(sol.maxProfit([2,1,3,4,1,2,1,5,4]))
