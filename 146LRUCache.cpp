#include <unordered_map>

struct Node{
int val;
int key;
Node *next;
Node *prev;

Node() : val(0), next(nullptr) {}
Node(int x, int y) : key(x), val(y), next(nullptr) {}
Node(int x) : val(x), next(nullptr) {}
Node(int x, Node *next) : val(x), next(next) {}
Node(int x, int y, Node *next, Node *prev) : key(x), val(y), next(next), prev(prev) {}
};

class LRUCache {
public:
    int cap;
    unordered_map<int, Node*> hash;
    Node* head;
    Node* tail;

    void remove(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    void insertAfterHead(Node* node) {
        node->next = head->next;
        node->prev = head;
        head->next->prev = node;
        head->next = node;
    }

    LRUCache(int capacity) {
        cap = capacity;
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
    }
    
    int get(int key) {
        if (hash.find(key) == hash.end()){
            return -1;
        }
        
        remove(hash[key]);
        insertAfterHead(hash[key]);
        return hash[key]->val;
    }
    
    void put(int key, int value) {
        if (hash.find(key) != hash.end()) {
            Node* node = hash[key];
            node->val = value;
            remove(node);
            insertAfterHead(node);
            return;
        }
        
        if (hash.size() == cap) {
            Node* lruNode = tail->prev; 
            hash.erase(lruNode->key);   
            remove(lruNode);            
            delete lruNode;             
        }
        
        Node* newNode = new Node(key, value);
        hash[key] = newNode;
        insertAfterHead(newNode);
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */