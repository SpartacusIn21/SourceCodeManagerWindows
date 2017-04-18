//Ref: 《编程之美》——分层遍历二叉树
//Author: Chen Yangchun
//Data: 2015/8/30
#include<iostream>
#include<vector>
#include<stack>
using namespace std;
/*使用层次遍历法遍历该二叉树
	                                   | 1 |
									  -    -
									-       -
								  | 2 |    | 3 |  
								  -  -         -
								-     -         -
							 | 4 |   | 5 |      | 6 |
*/
struct Node
{
	int data;
	Node* lChild;
	Node* rChild;
};
//层次遍历法递归代码，所有遍历都需要从根结点开始，效率比较低
int PrintNodeAtLevel(Node *root, int level)
{
	if(!root || level < 0)
	{
		return 0;
	}
	else if(level == 0 )
	{
		cout << root->data << " ";
		return 1;
	}
	return PrintNodeAtLevel(root -> lChild, level - 1) + PrintNodeAtLevel(root -> rChild, level - 1);//分层遍历，层次遍历的关键，@从左子树到右子树输出
	//return PrintNodeAtLevel(root -> rChild, level - 1) + PrintNodeAtLevel(root -> lChild, level - 1);//分层遍历，层次遍历的关键，@从右子树到左子树输出
}
//按层次遍历二叉树
//root:二叉树根节点
//不需要从根节点重复遍历，效率比较高
void PrintNodeByLevel(Node* root)
{
	if(root == NULL)
		return ;
	vector<Node*> vec;
	vec.push_back(root);
	int cur = 0;
	int last = 1;
	while(cur < vec.size())//整个BT的Level层循环
	{
		last = vec.size();
		while(cur < last)//当前Level层的各个节点循环
		{
			cout << vec[cur]->data << " ";
			if(vec[cur]->lChild)
				vec.push_back(vec[cur]->lChild);
			if(vec[cur]->rChild)
				vec.push_back(vec[cur]->rChild);
			cur++;

		}
		cout << endl;
	}


}
void PrintByReverseLevel(Node *root)//从下往上访问二叉树，待消化
{
	vector<Node *> q;
	stack<int> q2; //记录当前节点的层次
	Node *p;
	q.push_back(root);
	q2.push(0);
	int cur=0;
	int last=1;
	while(cur<q.size())
	{
		int level=q2.top();
		last=q.size();
		while(cur<last)
		{
			p=q[cur];
			if(p->rChild)
			{
				q.push_back(p->rChild);
				q2.push(level+1);
			}
			if(p->lChild)
			{
				q.push_back(p->lChild);
				q2.push(level+1);
			}
			cur++;
		}
	}
	while(!q2.empty())
	{
		cout << q[--cur]->data;
		int temp=q2.top();
		q2.pop();
		if(q2.empty() || temp!=q2.top())
			cout << endl;
	}
}
int main()
{
	//Init BT(Binary Tree)
	Node node1,node2,node3,node4,node5,node6;
	node4.data=4;
	node4.lChild=NULL;
	node4.rChild=NULL;
	node5.data=5;
	node5.lChild=NULL;
	node5.rChild=NULL;
	node2.data=2;
	node2.lChild=&node4;
	node2.rChild=&node5;
	node6.data=6;
	node6.lChild=NULL;
	node6.rChild=NULL;
	node3.data=3;
	node3.lChild=NULL;
	node3.rChild=&node6;
	node1.data=1;
	node1.lChild=&node2;
	node1.rChild=&node3;
	cout << "*******方法1********" <<endl;
	////层次遍历所有层，@知道树的深度
	//for(int i = 0; i < 3; i++)
	//{
	//	int Num = PrintNodeAtLevel(&node1,i);
	//	cout << "Num:" << Num <<endl;
	//}
	//层次遍历所有层，@不知道树的深度
	for(int i = 0; ; i++)
	{
		if(!PrintNodeAtLevel(&node1,i))//效率较低，因为每层都需要从根节点开始遍历
			break;
		cout << endl;
	}
	cout << "*******方法2********" <<endl;
	PrintNodeByLevel(&node1);//效率比较高，利用了队列概念，每层遍历时只需要上一层的信息即可
	cout << "*******方法1：从下往上********" <<endl;
	PrintByReverseLevel(&node1);//效率比较高，利用了队列概念，每层遍历时只需要上一层的信息即可
	getchar();
	return 0;
}