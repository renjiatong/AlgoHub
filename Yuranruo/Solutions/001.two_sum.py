#解法一：暴力
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
#解法二：Hash表
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]]=i
        for i in range(len(nums)):
            c=dic.get(target-nums[i])
            if c != None and i!=c:
                return[i,c]
#解法三：双指针
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp=nums.copy() #需先拷贝list，否则下标会变
        temp.sort()
        i=0
        j=len(nums)-1
        while i<j:      #双指针不断向内逼近
            if (temp[i]+temp[j])>target:
                j=j-1
            elif (temp[i]+temp[j])<target:
                i=i+1
            else:
                break
        m=nums.index(temp[i])
        nums.pop(m)     #预防两数相同的edge case,将上一个数弹出
        n=nums.index(temp[j])
        if n>=m:
            n=n+1       #弹出会导致后面的数字下标-1,故在此将后面数字的下标+1
        return [m,n]
