class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int length = 0;
        int prev = -9999;
        vector<int> copy;
        for (auto num : nums) {
            if (num == prev) {
                continue;
            } else {
                copy.push_back(num);
                prev = num;
                length++;
            }
        }
        for (int i = 0;i < length; i++) {
            nums[i] = copy[i];
        }
        return length;
    }
};

