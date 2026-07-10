/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

#include <cmath>

class Solution {
public:
    int heightTree(TreeNode* root){
        if (root == nullptr){
            return 0;
        }

        int ldepth = heightTree(root->left);
        int rdepth = heightTree(root->right);

        return 1 + max(ldepth, rdepth);
    }

    bool isBalanced(TreeNode* root) {

        if (root == nullptr){
            return true;
        }
        
        int lheight = heightTree(root->left);
        int rheight = heightTree(root->right);

        if( abs(lheight-rheight) == 1 || abs(lheight-rheight) == 0 ){
            if (root->right != nullptr && root->left != nullptr){
                return isBalanced(root->right) && isBalanced(root->left);
            }
            else if (root->left != nullptr){
                return isBalanced(root->left);
            }
            else if (root->right != nullptr){
                return isBalanced(root->right);
            }
        }
        else{
            return false;
        }

        return true;
    }
};