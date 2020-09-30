#方法一：暴力遍历，此法还有另一个邪道：使用python自带的count()函数直接统计0的个数，删去所有0再添加到末尾即可
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2: return nums
        i,k=0,0
        while k!=len(nums):
            if nums[i]==0:
                nums.append(0)
                del nums[i]
                i -= 1
            i += 1
            k += 1
        return nums
#方法二：快慢指针：快指针不停向后跑，遇到非零数则赋值给慢指针，慢指针向前进一步。最后将慢指针后面的所有数都赋值为0即可
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
           if nums[i] != 0:
                nums[j]=nums[i]
                j += 1
        for x in range(j,len(nums)):
            nums[x]=0 
        return nums
#方法三：还是快慢指针的思想，只不过当快指针遇到非零数后直接与慢指针交换数字，无需方法二最后的赋值过程
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        for i in range(len(nums)):
           if nums[i] != 0:
                nums[j],nums[i]=nums[i],nums[j]
                j += 1
        return nums
