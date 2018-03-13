#pragma once
#include<list>
#include "MyMutex.h"
#include "MyStack.h"
#include "MyList.h"
#include"MyQueue.h"
#include "Singleton.h"
class CMyThread;
class CTask;
enum PRIORITY
{
	NORMAL,
	HIGH
};
class CBaseThreadPool
{
public:
	virtual bool SwitchActiveThread(CMyThread*)=0;
};
class CMyThreadPool:public CBaseThreadPool
{
public:
	CMyThreadPool(int num=5);//线程池中线程数量
	~CMyThreadPool(void);
public:
	virtual CMyThread* PopIdleThread();
	virtual bool SwitchActiveThread(CMyThread*);
	virtual CTask*GetNewTask();
public:
	//priority为优先级。高优先级的任务将被插入到队首。
    bool addTask(const std::function<BOOL()>& fun,PRIORITY priority,int id=-1);
	bool addTask(CTask*t,PRIORITY priority);
    bool removeTask(int id);
	bool start();//开始调度。
	bool destroyThreadPool();
    bool clearThreadPool();

private:
	int m_nThreadNum;
	bool m_bIsExit;
	
	CMyStack m_IdleThreadStack;//Stack是后进先出的结构，Idel线程无所谓哪一个，方便拿出就可
	CMyList m_ActiveThreadList;//List是方便删除的结构，Active线程是同时运行的，并不知哪个线程先运行结束，所以要方便移除，用List最合适了
	CMyQueue m_TaskQueue;//queue和deque是顺序结构，先进先出，如果任务优先级都相同的，就使用queue，如果有两种优先级，就使用deque，如果有若干优先级，就使用multimap
};
template class Singleton<CMyThreadPool>;
#define THREADPOOL_MGR Singleton<CMyThreadPool>::GetInstance()
