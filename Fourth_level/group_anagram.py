
class Solution:
    def groupAnagrams(self, strs) :
        # dic={}
        # #val=[]
        # for i in strs:
        #     if ("".join(sorted(i))) in dic:
        #         dic["".join(sorted(i))].append(i)
        #     else:
        #         dic["".join(sorted(i))]=[i]
        # return list(dic.values())
        # not optimal as nlogn

        dic={}
        for i in strs:
            lis=[0]*26 #26 characters in ABC
            for chars in i:
                lis[ord(chars)-ord('a')]+=1 #ord gives ascii value of character
                #and we are subtracting character a(a is the first word) by order of the character i see in the string
                #this way i will find each character of the i , eat/tea/tan ...
                #i.e e, a and t ascii value and lis of that value is +1
                
                # i will have something like
                # lis[1,0,0,0,1,000000000000001,000000] - put comma, only at location of e ,a ,t for each input the value is 1, came only once
                # and so +1 happened only once.
                
                #now make this key of the dic, but not as is, as it has to be nonmutable
            lis=tuple(lis) #once all character are done then make the tuple
                #then store in dic
            if lis in dic:
                dic[lis].append(i)
            else:
                dic[lis]=[i]
        return list(dic.values())
        

sol=Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))