def knapsack(wt,val,W,n):
    if len(wt)==0:
        return 0

    memo={}
    #Deselect=0
    def dp(i,remaining_capacity):

        if i==n:
            return 0

        if (i,remaining_capacity) in memo:
            return memo[(i,remaining_capacity)]

        Deselect=dp(i+1,remaining_capacity)

        Select=0
        if wt[i]<=remaining_capacity:
            Select=val[i]+dp(i,remaining_capacity-wt[i])

        result=max(Select,Deselect)

        memo[(i,remaining_capacity)]=result

        return result

    answer=dp(0,W)

    return answer
