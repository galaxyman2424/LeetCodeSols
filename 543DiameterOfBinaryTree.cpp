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
class Solution {
public:

    int maxdiameter;

    int diameterOfBinaryTree(TreeNode* root) {
        calculateHeight(root);
        return maxdiameter;
    }

    int calculateHeight(TreeNode* node){
        if (node == nullptr){
            return 0;
        }

        int lheight = calculateHeight(node->left);
        int rheight = calculateHeight(node->right);

        maxdiameter = max(maxdiameter, lheight + rheight);

        return max(lheight, rheight) + 1;
    }
};