#这道题本质就是斐波那契额数列。。。所以直接硬算或者带公式即可
#硬算，会超时，因此加上了缓存修饰器
class Solution1:
    @lru_cache()       #缓存装饰器 https://docs.python.org/zh-cn/3/library/functools.html
    def climbStairs(self, n: int) -> int:
        if n==1: return 1
        elif n==2: return 2
        else:
            return self.climbStairs(n-1)+self.climbStairs(n-2)
#带公式即可
class Solution2:
    import math
    def climbStairs(self, n: int) -> int:
        rootfive=5**0.5
        fn=(((1+rootfive)/2)**(n+1)-((1-rootfive)/2)**(n+1))/rootfive
        return int(fn)      #会有计算精度的问题，因此要转成int型
#利用斐波那契额数量的特性之一，即n=(n-1)+(n-2)，那么并不需要解法1中这么大的缓存，只需记住前两个解即可
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        a,b=1,2
        for i in range(3,n+1):
            a,b=b,a+b
        return b