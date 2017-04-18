// udptest.h : main header file for the UDPTEST application
//

#if !defined(AFX_UDPTEST_H__F3CCB4A9_E2FF_47A6_8B35_4F84D0ECE78B__INCLUDED_)
#define AFX_UDPTEST_H__F3CCB4A9_E2FF_47A6_8B35_4F84D0ECE78B__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols

/////////////////////////////////////////////////////////////////////////////
// CUdptestApp:
// See udptest.cpp for the implementation of this class
//

class CUdptestApp : public CWinApp
{
public:
	CUdptestApp();

// Overrides
	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CUdptestApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// Implementation

	//{{AFX_MSG(CUdptestApp)
		// NOTE - the ClassWizard will add and remove member functions here.
		//    DO NOT EDIT what you see in these blocks of generated code !
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_UDPTEST_H__F3CCB4A9_E2FF_47A6_8B35_4F84D0ECE78B__INCLUDED_)
