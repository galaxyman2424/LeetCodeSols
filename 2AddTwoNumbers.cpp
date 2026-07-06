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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        int carry = 0;
        ListNode* newhead = new ListNode();
        ListNode* curr = newhead;


        while (l1 != nullptr and l2 != nullptr){
            int tot = l1->val + l2->val + carry;
            curr->val = tot%10;
            carry = tot/10;

            l1 = l1->next;
            l2 = l2->next;

            if(l1 != nullptr || l2 != nullptr){
                curr->next = new ListNode();
                curr = curr->next;
            }
        }

        while (l1 != nullptr){
            int tot = l1->val + carry;
            curr->val = tot%10;
            carry = tot/10;

            l1 = l1->next;

            if(l1 != nullptr){
                curr->next = new ListNode();
                curr = curr->next;
            }
        }

        while (l2 != nullptr){
            int tot = l2->val + carry;
            curr->val = tot%10;
            carry = tot/10;

            l2 = l2->next;

            if(l2 != nullptr){
                curr->next = new ListNode();
                curr = curr->next;
            }
        }

        if (carry > 0){
            curr->next = new ListNode(carry);
        }

        return newhead;
    }
};