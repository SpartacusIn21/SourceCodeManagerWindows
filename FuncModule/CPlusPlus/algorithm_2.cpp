/*
@que:一个二叉树，数的节点组成一个数组、作为方法的输入，每个节点里除了和其他节点的关联关系字段之外，还有当前节点在显示器上的坐标，其中y坐标一定等于当前节点在树中的层数（例如y坐标等于2则一定是在树的第二层）；请写一个方法判断在显示这个树时，有没有树枝会交叉。
@author:yangchun,chen
@date:3/26/2018
@pudong,shanghai
*/
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

struct TreeNode{
	int x,y;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x,int y):x(x),y(y),left(nullptr),right(nullptr){}
};
/*参考LevelTraverseOfBt工程层次遍历*/
bool LayerTraversal(TreeNode *root){
	if(!root){
		return true;
	}	
	vector<TreeNode *> vec;
	int cur = 0,last = 0;
	TreeNode *last_node = root;
	vec.push_back(root);
	bool result = false;
	//遍历整棵树
	while(cur < vec.size()){
		last = vec.size();
		//遍历二叉树的一层
		while(cur < last){
			//如果位于同一层，而且左边的节点x值比右边的大，树枝就会有交叉
			if(last_node->y == vec[cur]->y){
				result = last_node->x > vec[cur]->x;
				if(result)
					break;
			}
			last_node = vec[cur];
			//将下一层的节点入队列
			if(vec[cur]->left){
				vec.push_back(vec[cur]->left);
			}	
			if(vec[cur]->right){
				vec.push_back(vec[cur]->right);
			}	
			cur++;
		}
		if(result){
			break;
		}
		
	}
	return result;
}

int main(){
	TreeNode n1(1,0);
	TreeNode n2(9,1);
	TreeNode n3(10,1);
	TreeNode n4(4,2);
	TreeNode n5(5,2);
	n1.left = &n2;
	n1.right = &n3;
	n2.left = &n4;
	n2.right = &n5;
	bool result = LayerTraversal(&n1);
	cout << "The binary tree " << (result ? "has " : "don't have ") << "overlap area!" << endl;
	return 0;
}
