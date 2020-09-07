/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if (head == NULL) {
            return head;
        }
        ListNode* res = head;
        while (head->next!= NULL && head->next->next!= NULL) {
            int temp1 = head->val;
            int temp2 = head->next->val;
            head->val = temp2;
            head->next->val = temp1;
            head = head->next->next;
            //head = head->next;
        }
        if (head->next!= NULL && head->next->next== NULL) {
            int temp1 = head->val;
            int temp2 = head->next->val;
            head->val = temp2;
            head->next->val = temp1;
        }
        return res;
    }
};
