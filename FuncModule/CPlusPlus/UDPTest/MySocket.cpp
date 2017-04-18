// MySocket.cpp : implementation file
//

#include "stdafx.h"
#include "udptest.h"
#include "MySocket.h"
#include "udptestDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// MySocket

MySocket::MySocket()
{
}
MySocket::MySocket(CUdptestDlg* p_hwnd)
{
	p_dlgwnd=p_hwnd;
}
MySocket::~MySocket()
{
}


// Do not edit the following lines, which are needed by ClassWizard.
#if 0
BEGIN_MESSAGE_MAP(MySocket, CSocket)
	//{{AFX_MSG_MAP(MySocket)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()
#endif	// 0

/////////////////////////////////////////////////////////////////////////////
// MySocket member functions

void MySocket::OnReceive(int nErrorCode) 
{
	// TODO: Add your specialized code here and/or call the base class
	
	CSocket::OnReceive(nErrorCode);
	p_dlgwnd->OnReceive(this);
}
