// TabExampleDlg.h : header file
//

#pragma once
#include "afxcmn.h"

#include "MyTabCtrl.h" ////////do this


// CTabExampleDlg dialog
class CTabExampleDlg : public CDialog
{
// Construction
public:
	CTabExampleDlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	enum { IDD = IDD_TABEXAMPLE_DIALOG };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support


// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	//CTabCtrl m_cTab;
	CMyTabCtrl m_cTab; ////do this

	LRESULT ButtonPressed(WPARAM w, LPARAM l);////do this
};
