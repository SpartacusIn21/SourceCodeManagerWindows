/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
	vector<int> temp;
    int LevelTravase(TreeNode* root, int level)
    {
        if(root == NULL || level < 0)
            return 0;
        else if(level == 0)
        {
            temp.push_back(root->val);
            return 1;
        }
        return LevelTravase(root->left, level-1) + LevelTravase(root->right, level-1);
        
    }
    vector<vector<int>> levelOrder(TreeNode* root) {
        for(int level = 0; ; level++)
        {
            if(!LevelTravase(root,level))
                break;
            result.push_back(temp);
            temp.clear();
        }
        return result;
            
    }
 
 
    TreeNode* Find(TreeNode* root, TreeNode*p)//Find the p TreeNode in BST root
    {
        if(root == NULL)
            return NULL;
        else if(p->val < root->val)
        {
            return Find(root->left, p);
        }
        else if(p->val > root->val)
        {
            return Find(root->right, p);
        } vector<vector<int>> result;    
        else
            return root;
    }



/**
@question:https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 //二叉树的lowest common ancestor(LCA)的查找函数lowestCommonAncestor,深刻理解递归调用中局部变量和return语句层层返回的机制，大师级代码
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        
        if (root == p || root == q || root == NULL) return root;//1 这份代码最骚的地方在第一个判断这里，比如从root分成两个分支，如果p和q都不在左分支，那么最终递归后左分支返回NULL，结果就从右分支查找了
        TreeNode *left = lowestCommonAncestor(root->left, p, q), *right = lowestCommonAncestor(root->right, p, q);//后序遍历，这里left和right都是局部变量，每调用一次都会创建一次，但是通过//1和//2保证了找到的节点会层层返回到最开始的root节点那层的lowestCommonAncestor函数，大师级代码
        return left && right ? root : left ? left : right;//2  
    }
};