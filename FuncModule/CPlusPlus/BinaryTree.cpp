/*
FileName: BinaryTree.cpp
Create Time:   2015/09/03
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference:  https://leetcode.com/problems/minimum-depth-of-binary-tree/   
Question:Given a binary tree, find its minimum depth.The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
//方法1
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        //这两条语句是为了避免因为某个子树为空而直接返回零，而此时这种情况并不满足要求，因为不是叶节点，在求最小深度的时候不能缺，求最大深度的时候可缺
		if(!root->left) return 1 + minDepth(root->right);//
        if(!root->right) return 1 + minDepth(root->left);
        return 1+min(minDepth(root->left),minDepth(root->right));//这样代码只会被最后执行一次
    }
};
//方法2：高效算法
class Solution {
	int minDepth(TreeNode* root) {
		if (root == NULL) return 0;
		queue<TreeNode*> Q;
		Q.push(root);
		int i = 0;
		while (!Q.empty()) {
			i++;
			int k = Q.size();
			for (int j=0; j<k; j++) {
				TreeNode* rt = Q.front();
				if (rt->left) Q.push(rt->left);
				if (rt->right) Q.push(rt->right);
				Q.pop();
				if (rt->left==NULL && rt->right==NULL) return i;
			}
		}
		return -1; //For the compiler thing. The code never runs here.
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