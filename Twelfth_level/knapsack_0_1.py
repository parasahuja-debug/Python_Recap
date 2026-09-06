# 0/1 Knapsack Problem

# Problem:
# You are given n items, each with a weight wt[i] and a value val[i]. 
# You have a knapsack that can carry a maximum weight of W.

# Determine the maximum total value you can achieve 
# by selecting a subset of items such that the total weight does not exceed W. 
# For each item, you can either take it entirely or leave it — 
# you cannot take a fraction of an item, 
# and you cannot take an item more than once (hence "0/1").

# n = 4
# wt  = [1, 3, 4, 5]
# val = [1, 4, 5, 7]
# W = 7

def knapsack(wt,val,W,n):
    if len(wt)==0:
        return 0

    memo={}

    def dp(i,remaining_capacity):

        if i==n:
            return 0

        if (i,remaining_capacity) in memo:
            return memo[(i,remaining_capacity)]

        Deselect=dp(i+1,remaining_capacity)

        Select=0
        if wt[i]<=remaining_capacity:
            Select=val[i]+dp(i+1,remaining_capacity-wt[i])

        result=max(Select,Deselect)

        memo[(i,remaining_capacity)]=result

        return result

    answer=dp(0,W)

    return answer



