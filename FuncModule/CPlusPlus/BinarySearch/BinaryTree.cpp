/*
FileName: BinaryTree.cpp
Create Time:   2015/09/03
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  https://leetcode.com/problems/minimum-depth-of-binary-tree/   
Description: （1）二叉树的最小深度、最大深度递归算法；
*/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//求二叉树的最小深度
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        if(!root->left) return 1 + minDepth(root->right);//这两条语句是为了避免因为某个子树为空而直接返回零，而此时这种情况并不满足要求，因为不是叶节点，在求最小深度的时候不能缺，求最大深度的时候可缺
        if(!root->right) return 1 + minDepth(root->left);
        return 1+min(minDepth(root->left),minDepth(root->right));
    }
};


//求二叉树的最大深度，方法1和方法2其实是一样的，只是形式稍微有点不同而已
//方法1
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
/*         if(!root->left) return 1 + maxDepth(root->right);//这两条语句是为了避免因为某个子树为空而直接返回零，而此时这种情况并不满足要求，因为不是叶节点，在求最小深度的时候不能缺，求最大深度的时候可缺
        if(!root->right) return 1 + maxDepth(root->left); */
        return 1+max(maxDepth(root->left),maxDepth(root->right));
    }
};
//方法2
class Solution {
public:
    int maxDepth(TreeNode *root) {
        return root == NULL ? 0 : max(maxDepth(root -> left), maxDepth(root -> right)) + 1;//采用后续遍历
    }
};