#include <iostream>
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
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;
        
        // first lets find the middle of the list
        // we will use a fast and a fastfast pointer, when fastfast finds the end fast is at the middle

        ListNode* fast = head;
        ListNode* fastfast = head;

        while (fastfast->next != NULL && fastfast->next->next != NULL){
            fastfast = fastfast->next->next;
            fast = fast->next; 
        }

        // now we should reverse the last part of the list, i am going to steal my reverse a linked list code
        //fast is at the middle

        ListNode* prev = NULL;
        ListNode* curr = fast->next;
        fast->next = NULL;

        while (curr != NULL){
            ListNode* nxt = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nxt;
        }

        //prev is now the head of our reversed second half of our list

        ListNode* split = prev;
        // I want to keep split so we know where the beginging of the second half of the list is

        ListNode* fh = head; //first half
        ListNode* sh = prev; //second half
        while(sh != NULL){
            ListNode* temp = fh->next;
            ListNode* temp2 = sh->next;

            fh->next = sh;
            sh->next = temp;

            fh = temp;
            sh = temp2;

        }
    }
};