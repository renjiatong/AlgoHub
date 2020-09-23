Two Sum有三种经典做法，最直观的暴力法直接两层循环即可，无需多言。
## Hash表
two sum的正确理解应是target - nums[1] = nums[2]，故将nums存入Hash表[^1]中，每次查询nums[2]即可。

## 双指针法
双指针法是经典的求解思路，在很多问题中都会遇到，用在Two Sum上有些大材小用。。。

1. 先将整个数组复制后排序，直接.sort即可

2. 设置两个变量 i, j，分别在首尾进行逼近。
   
   ```python
       if temp[i]+temp[j]>target:
           j=j-1
       elif temp[i]+temp[j]<target:
           i=i-1
   ```

3. 再考虑各种edge case进行优化即可









[^1]:python中的字典就是hash