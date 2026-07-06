#include <iostream>
#include <unordered_map>

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {

        unordered_map<Node*, Node*> res; 
        Node* curr = head;

        //first pass
        while (curr != nullptr){
            res[curr] = new Node(curr->val);
            curr = curr-> next;
        }

        //second pass
        Node* curr2 = head;
        while(curr2 != nullptr){
            res[curr2]->next = res[curr2->next];
            res[curr2]->random = res[curr2->random];
            curr2 = curr2->next;
        }

        

        return res[head];
    }
};