# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         #return x ** n
       
#         result=1
#         isngeative=False
#         if n<0:
#             n=-n
#             isngeative=True
#         for i in range(n):
#             result*=x
#         if isngeative:
#             return 1/result
#         else:
#             return result

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x ** n
        # result=None
        # for i in range(n):
        #     if result==None:
        #         result=2
        # 
        negative = n < 0

        if negative:
            n = -n

        result = 1

        while n > 0:
            if n % 2 == 1: #only when odd we need extra multiple
                result *= x

            x *= x #core
            n //= 2#core

        if negative:
            return 1 / result

        return result