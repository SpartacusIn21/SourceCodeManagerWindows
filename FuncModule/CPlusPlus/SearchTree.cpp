/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
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
        else
            return root;
    }



/**
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
        
        if (root == p || root == q || root == NULL) return root;//1
        TreeNode *left = lowestCommonAncestor(root->left, p, q), *right = lowestCommonAncestor(root->right, p, q);//后序遍历，这里left和right都是局部变量，每调用一次都会创建一次，但是通过//1和//2保证了找到的节点会层层返回到最开始的root节点那层的lowestCommonAncestor函数，大师级代码
        return left && right ? root : left ? left : right;//2
    }
};