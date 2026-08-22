class Solution:
    def maxArea(self, height) -> int:
        if len(height)<1:
            return 0
        max_area=float("-inf")
        left=0
        right=len(height)-1
        while left<right:
            # print(left)
            # print(right)
            print(height[left],height[right],right-left)
            area=min(height[left],height[right])*(right-left)
            max_area=max(max_area,area)
            print(area,max_area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area
# traverse the height
# pointer left and right
# while left<right
# left element and right element
# max(min height(left and right) * right-left+1 - 9,)
# whichever is less left and right
# ++
