/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {

        ListNode* res = new ListNode();
        ListNode* return_res = res;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val <= l2->val) {
                res->val = l1->val;
                res->next = new ListNode();
                res = res->next;
                l1 = l1-> next;
            } else if (l1->val > l2->val) {
                res->val = l2->val;
                res->next = new ListNode();
                res = res->next;
                l2 = l2-> next;
            }
        }

        if (l1 == NULL && l2 == NULL) {
            return NULL;
        }
        if (l1 == NULL) {
            res->val = l2->val;
            res->next = l2->next;
        }
        if (l2 == NULL) {
            res->val = l1->val;
            res->next = l1->next;
        }


        return return_res;
    }
};
