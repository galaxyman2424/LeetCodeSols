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
    bool hasCycle(ListNode *head) {
        if (nullptr == head || nullptr == head->next){
            return false;
        }


        ListNode* currn = head;
        ListNode* currnn = head;

        while (currnn != NULL && currnn->next != NULL && currnn->next->next != NULL){
            currn = currn->next;
            currnn = currnn->next->next;
            
            if (currn == currnn){
                return true;
            }
        }
        return false;
    }
};