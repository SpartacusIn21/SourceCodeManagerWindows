// udptestDlg.h : header file
//

#if !defined(AFX_UDPTESTDLG_H__7E2C6E83_4759_4488_9A5B_3A19CB180FF9__INCLUDED_)
#define AFX_UDPTESTDLG_H__7E2C6E83_4759_4488_9A5B_3A19CB180FF9__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#include "mysocket.h"
/////////////////////////////////////////////////////////////////////////////
// CUdptestDlg dialog

class CUdptestDlg : public CDialog
{
// Construction
public:
	void OnReceive(MySocket *sock);
	CUdptestDlg(CWnd* pParent = NULL);	// standard constructor
	MySocket* m_MySocket;
// Dialog Data
	//{{AFX_DATA(CUdptestDlg)
	enum { IDD = IDD_UDPTEST_DIALOG };
		// NOTE: the ClassWizard will add data members here
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CUdptestDlg)
	public:
	virtual BOOL DestroyWindow();
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CUdptestDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnButton1();
	afx_msg void OnTimer(UINT nIDEvent);
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_UDPTESTDLG_H__7E2C6E83_4759_4488_9A5B_3A19CB180FF9__INCLUDED_)
