"""
So, here we are given an array and we have to actually return another array
the returned array will be a product of all other numbers except self.
[1,2,3,4] - [24,12,8,6]
"""
# def product_except_self(lis):
#     arr_new=[0]*len(lis)
#     mul=1
#     for i in range(len(lis)):
#         arr_new[i]=mul*lis[i]
#         mul=arr_new[i]
    
#     for j in range(len(lis)):
#         arr_new[j]=arr_new[len(lis)-1]//lis[j]
   

#     return arr_new

def product_except_self(nums):
    
    result = [1] * len(nums)
    #result_s=[1]*len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix #calulating prefix of the current number, first index would be
        #always 1,
        prefix *= nums[i] #now multiplying , so that next can be given prefix value 
        #in line 25
        print(result,prefix)

    suffix = 1
    """ this is with space complexity O(n)
    for i in range(len(nums)-1, -1, -1):
        result_s[i]=suffix
        suffix*=nums[i]
    
    for i in range(len(nums)):
        result[i]=result[i]*result_s[i]

    return result
"""
    for i in range(len(nums)-1, -1, -1):
        #last of result(as per the loop) will be the same as last of prefix 
        result[i] *= suffix #result[i] in 38 line is multiplied with suffix,
        #result array is actually prefix array now before multiplying
        #and to calculate we are multiplying prefix with suffix
        #the thing to understand is we are starting from back meaning
        #we have to calculate suffix also along the way
        suffix *= nums[i] #suffix is calculated in 35 line 
        #combination of below two loops happen in last loop
        #now we are updating suffix value to get the next element in next iteration
    
    return result

print(product_except_self([1,2,3,4]))



