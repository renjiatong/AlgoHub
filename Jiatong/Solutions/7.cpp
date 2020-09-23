// 0ms 100%
// 5.8MB 92.44%
class Solution {
public:
    int reverse(int x) {
        bool neg = false;
        bool start = false;
        int res = 0;

        if (x == -2147483648) return 0;
        if (x == 0) return res;
        if (x < 0) {
            neg = true;
            x = -1 * x;
        }
        
        while(x!=0) {
            int a = x % 10;
            if (a == 0 && start == false) {              
                x = x / 10;
                continue;
            } else {
                start = true;
            }
            if (res > INT_MAX / 10) return 0;
            if (res < INT_MIN / 10) return 0;
            res = res * 10 + a;
            x = x / 10;
        }

        if (neg) {
            res = -1 * res;
        }
        
        return res;
        
    }
};
