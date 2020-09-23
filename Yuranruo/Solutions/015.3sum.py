#解法一：暴力解法——是不可能通过的XD
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stro=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0 and [nums[i], nums[j], nums[k]] not in stro:
                        stro.append([nums[i], nums[j], nums[k]])
        return stro
#解法二：双Hash
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
            
        nums.sort()
        dic={}
        for i,x in enumerate(nums):
            dic[-x]=i

        res=[]
        rhash={}
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]: 
                continue
            for j,b in enumerate(nums[i+1:]):       #list[i:]即从第i+1个元素开始截取列表
                if a+b in dic:
                    dic_index=dic[a+b]
                    if dic_index==i or dic_index==i+1+j:    #j从i+1开始，i+1+j即第二个数在nums中的位置
                        continue
                    va=sorted([a, b, nums[dic_index]])
                    key=",".join([str(x) for x in va])      #"".join()用于连接字符串
                    if key not in rhash:
                        res.append(va)
                        rhash[key]=True
        return res

#解法3：双指针————标准解法，居然更慢。。。
class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
           return []
        nums.sort()
        res=[]
        k=0
        for k in range(len(nums)-2):    #3sum至少需要3个数字，故到len(nums)-2即刻====即可
            if nums[k]>0: break
            if k>0 and nums[k]==nums[k-1]: continue

            i=k+1
            j=len(nums)-1
            while i < j:
                s=nums[i]+nums[j]+nums[k]
                if s>0:
                    j -= 1
                    while i<j and nums[j]==nums[j+1]:
                        j -= 1
                elif s<0:
                    i += 1
                    while i<j and nums[i]==nums[i-1]:
                        i += 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i<j and nums[j]==nums[j+1]:       #此处的while可以减少s的计算次数，加快速度
                        j -= 1
                    while i<j and nums[i]==nums[i-1]:
                        i += 1
        return res