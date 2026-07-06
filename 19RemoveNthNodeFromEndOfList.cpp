#include <iostream>
/**
 
Definition for singly-linked list.
struct ListNode {
int val;
ListNode *next;
ListNode() : val(0), next(nullptr) {}
ListNode(int x) : val(x), next(nullptr) {}
ListNode(int x, ListNode *next) : val(x), next(next) {}
};*/
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if (head->next == NULL){
            ListNode* edgecase = nullptr;
            return edgecase;
        }

        ListNode* end = head;
        ListNode* curr = head;

        int left = 1;
        int right = 1;

        while(end != nullptr){
            //cout << right << " <-right value left value-> "<< left  << " \n";
            //cout << right - n + 1 << " inqueality\n";
            if (left >= right - n + 1){
                
                right += 1;
                end = end->next;
            }
            else{
                left += 1;
                right += 1;
                end = end->next;
                curr = curr->next;
            }
        }

        //curr is currently at the node we want to get rid of
        // we should just iterate up tot it and then remove it
        
        //there should always bee an element after or else we would not have gotten to this part of the code due tot he first if statement
        if (curr == head){
            return head->next;
        }

        //if there are no elements after then we just remove it

        ListNode* tail = head;

        while(tail->next != curr){
            tail = tail->next;
        }
        cout << tail->val << " " << curr->val << "\n";

        if (curr->next == nullptr){
            tail->next = nullptr;
        }
        else if (curr->next){
            ListNode* temp = curr->next;
            curr->next = nullptr;
            tail->next = temp;
        }

        //now if there are elements after we have to walk up a pointer


        return head;
    }
};