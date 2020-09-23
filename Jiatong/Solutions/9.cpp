class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;

        int temp = x;
        bool start = false;
        int reverseNum = 0;

        while(x != 0) {
            int curr = x % 10;
            if (start == false && curr == 0) {
                return false;
            }
            start = true;
            if (reverseNum > (INT_MAX / 10)) return false;
            reverseNum = reverseNum*10 + curr;
            x = x / 10;
        }

        if (reverseNum == temp) {
            return true;
        } else {
            return false;
        }
    }
};
