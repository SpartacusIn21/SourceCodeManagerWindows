/*
FileName: BinaryTreeRightSizeView.cpp
Create Time:   2015/09/04
Modify Time: 
Author: Chen Yangchun
Owner:  Chen Yangchun
Place:  上海交通大学闵行校区微电子楼301室
Reference: https://leetcode.com/problems/binary-tree-right-side-view/
Description: （1）使用层次遍历算法输出从右边往左看到的二叉树的结点值；
*/
/*
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

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
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {//BFS算法，层次遍历
        if(!root)return ret;
		queue<TreeNode*>mQ;//新建队列
        vector<int> ret;//用来存储输出结果        
        mQ.push(root);//入队列
        while(!mQ.empty()){//当队列不为空时
            ret.push_back(mQ.back()->val);//将队列中最后一个元素push_back到vector中，因为最后一个节点是始终是该层中从右边能看到的那个元素，这是由后面的遍历决定的
            for(int i=mQ.size();i>0;i--){
                TreeNode *tn=mQ.front();
                mQ.pop();
                if(tn->left)mQ.push(tn->left);//先让左子树入队，再让右子树入队，可保证队列中最后一个元素是满足要求的
                if(tn->right)mQ.push(tn->right);
            }
        }
        return ret;
    }
};