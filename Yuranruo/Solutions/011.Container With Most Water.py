#方法一：双指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater,temp,i,j=0,0,0,len(height)-1
        while i<j:
            d=j-i
            maxwater=min(height[i],height[j])*d
            if maxwater>temp : temp=maxwater
            if height[i]<=height[j]:  i += 1  #一开始不知道左右指针谁应该先移动，后来发现移动短的即可
            else : j -= 1
        return temp
#方法二：暴力
#会超出时间限制，就不贴了XD
