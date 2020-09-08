class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int count = 0;
        vector<int> copy;
        for (auto num : nums) {
            if (num == val) {
                continue;
            } else {
                count++;
                copy.push_back(num);
            }
        }
        for (int i = 0; i < count; i++) {
            nums[i] = copy[i];
        }
        return count;
    }
};
