class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0]) #sorting so that we can equate and
        #if multiple lists are there and we need to merge intervals, its easy
        result=[] #storing vec
        first_list=intervals[0]
        for i in range(1,len(intervals)):
            secondlist=intervals[i]
            if first_list[1]>=secondlist[0]:#compare the last of frist element
                #and 1st of last element
                first_list[1]=max(secondlist[1],first_list[1])#keep the max as last
                #value
            else:
                result.append(first_list)#if the values are not coniciding,add to result and move forward
                first_list=secondlist #now compare with the secondlist
        result.append(first_list)#append the last list to the vec
        return result
            

# [1,3],[2,6],[8,10],[15,18] input
# [1,6],[8,10],[15,18] output
# so, firstlist[1]>=secondlist[0] and firstlist[1]<=secondlist[1]
# firstlist[0],secondlist[1] append to a list