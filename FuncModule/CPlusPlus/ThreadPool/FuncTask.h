#pragma once
#include "task.h"
class CFuncask :
	public CTask
{
public:
	CFuncask(int id);
	~CFuncask(void);
public:
    void SetTaskFunc(std::function<BOOL()> func);
    virtual void taskProc();
private:
    std::function<BOOL()> m_fun;
};

