#if !defined(AFX_MYSOCKET_H__E39F2BBA_78C6_406A_A56F_FDA8541856D5__INCLUDED_)
#define AFX_MYSOCKET_H__E39F2BBA_78C6_406A_A56F_FDA8541856D5__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000
// MySocket.h : header file
//

class CUdptestDlg;

/////////////////////////////////////////////////////////////////////////////
// MySocket command target

class MySocket : public CSocket
{
// Attributes
public:

// Operations
public:
	MySocket();
	MySocket(CUdptestDlg* p_hwnd);
	virtual ~MySocket();

// Overrides
public:
	CUdptestDlg* p_dlgwnd;
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(MySocket)
	public:
	virtual void OnReceive(int nErrorCode);
	//}}AFX_VIRTUAL

	// Generated message map functions
	//{{AFX_MSG(MySocket)
		// NOTE - the ClassWizard will add and remove member functions here.
	//}}AFX_MSG

// Implementation
protected:
};

/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_MYSOCKET_H__E39F2BBA_78C6_406A_A56F_FDA8541856D5__INCLUDED_)
