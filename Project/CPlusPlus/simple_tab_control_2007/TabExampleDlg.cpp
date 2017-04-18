// TabExampleDlg.cpp : implementation file
//

#include "stdafx.h"
#include "TabExample.h"
#include "TabExampleDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CTabExampleDlg dialog



CTabExampleDlg::CTabExampleDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CTabExampleDlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CTabExampleDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_TAB1, m_cTab);
}

BEGIN_MESSAGE_MAP(CTabExampleDlg, CDialog)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_MESSAGE(WM_BUTTONPRESSED,ButtonPressed) ////do this
END_MESSAGE_MAP()


// CTabExampleDlg message handlers

BOOL CTabExampleDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here
	m_cTab.Init();

	m_cTab.InsertItem(0,"Connections");
	m_cTab.InsertItem(1,"Notifications");
	m_cTab.InsertItem(2,"Transfers");
	m_cTab.InsertItem(3,"Advanced");

	//CONNECTIONS
	m_cTab.CreateGroupBox("Startup",1,0,310,52);
	m_cTab.CreateCheckBox(FALSE,"Start Program with Windows", 2, 0, 0, 10, 15);
	m_cTab.CreateCheckBox(FALSE,"Connect to All Contacts on Startup", 3, 0, P_BELOW | P_LEFT);

	m_cTab.CreateGroupBox("New Contact Acceptance", 4, 0, 310, 52, P_BELOW, 0, 10);
	m_cTab.CreateRadioBox(FALSE,"Auto Accept All New Contacts", 5, 0, P_LEFT | P_TOP, 10, 15, WS_GROUP);
	m_cTab.CreateRadioBox(TRUE,"New Contacts Must Match Connection Password", 6, 0, P_BELOW | P_LEFT, 0, 0, 0);

	m_cTab.CreateGroupBox("Connection Password", 7, 0, 310, 52, P_BELOW, 0, 10);
	m_cTab.CreateEdit(FALSE,8, 0, P_TOP, 10, 20, 290);
	((CEdit*)m_cTab.GetDlgItem(8))->SetCueBanner(L"  To create a password, type one here");
	//note cuebanner requires you to set WINVER 0x0500, _WIN32_WINNT 0x0501, _WIN32_WINDOWS 0x0500, _WIN32_IE 0x0500

	//NOTIFICATIONS
	m_cTab.CreateGroupBox("Sounds",8,1,310,52);
	m_cTab.CreateCheckBox(FALSE,"Play Sound When Contact Comes Online", 9, 1, 0, 10, 15);
	m_cTab.CreateCheckBox(FALSE,"Play Sound On New Messages", 10, 1, P_BELOW | P_LEFT);

	m_cTab.CreateGroupBox("Visual", 11, 1, 310, 105, P_BELOW, 0, 10);
	m_cTab.CreateCheckBox(FALSE,"Flash Taskbar Button When Messages", 12, 1, P_LEFT | P_TOP, 10, 15);
	m_cTab.CreateCheckBox(FALSE,"Enable \"Idle\" Away Message for me", 13, 1, P_BELOW | P_LEFT, 0, 0);
	m_cTab.CreateCheckBox(FALSE,"Animate When Contacts Come Online", 14, 1, P_BELOW | P_LEFT, 0, 0);
	m_cTab.CreateCheckBox(FALSE,"Animate On New Messages", 15, 1, P_BELOW | P_LEFT, 0, 0);
	m_cTab.CreateCheckBox(TRUE,"Animate When Contacts Browse My Files", 16, 1, P_BELOW | P_LEFT, 0, 0);

	m_cTab.CreateGroupBox("Program Updates", 11, 1, 310, 40, P_BELOW, 0, 10);
	m_cTab.CreateCheckBox(TRUE,"Automatically Check For Updates", 17, 1, P_LEFT | P_TOP, 10, 15);

	//FILE TRANSFERS
	m_cTab.CreateGroupBox("Transfer Options", 18,2,310,120);
	m_cTab.CreateCheckBox(FALSE,"Enable Folder Sharing", 19, 2, 0, 10, 15);
	m_cTab.CreateCheckBox(FALSE,"Auto Save Incoming Files and Folders", 20, 2, P_BELOW | P_LEFT, 0, 8);
	m_cTab.CreateCheckBox(FALSE,"Only Auto Save From Specific Contacts", 21, 2, P_BELOW | P_LEFT, 0, 8);
	m_cTab.CreateCheckBox(TRUE,"Create AutoSave Subdirectories for Peers", 22, 2, P_BELOW | P_LEFT, 0, 8);

	m_cTab.CreateButton("Select1",23,2, 0, m_cTab.RightOf(22)+15, m_cTab.TopOf(19),60);
	m_cTab.CreateButton("Select2",24,2,P_LEFT,0, m_cTab.TopOf(20) ,60);
	m_cTab.CreateButton("Select3",25,2,P_LEFT,0, m_cTab.TopOf(21) ,60);

	//ADVANCED
	m_cTab.CreateGroupBox("Select Your Internet Connection Type",26,3,310,52);
	m_cTab.CreateRadioBox(FALSE,"Static IP (Cable Modems, T1, T3)", 27, 3, 0, 10, 15, WS_GROUP);
	m_cTab.CreateRadioBox(TRUE,"Dynamic IP (DSL, ISDN, Dialup, Satellite)", 28, 3, P_BELOW | P_LEFT, 0, 0, 0);

	m_cTab.CreateGroupBox("Encryption Key", 29, 3, 310, 52, P_BELOW, 0, 10);
	m_cTab.CreateEdit("1234MYKEY", 30, 3, P_TOP, 10, 20, 290);

	m_cTab.CreateGroupBox("Data Port (1-65535)", 31, 3, 120, 52, P_BELOW, 0, 20);
	m_cTab.CreateEdit("9000", 32, 3, P_TOP, 10, 20, 100);
	((CEdit*)m_cTab.GetDlgItem(32))->SetLimitText(5);
	((CEdit*)m_cTab.GetDlgItem(32))->ModifyStyle(0,ES_NUMBER);

	m_cTab.CreateGroupBox("Translucency (1-255)", 33, 3, 120, 52, 0, m_cTab.RightOf(31)+70, m_cTab.TopOf(31));
	m_cTab.CreateEdit("191", 34, 3, P_TOP | P_LEFT, 10, 20, 100);
	((CEdit*)m_cTab.GetDlgItem(34))->SetLimitText(3);
	((CEdit*)m_cTab.GetDlgItem(34))->ModifyStyle(0,ES_NUMBER);
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

LRESULT CTabExampleDlg::ButtonPressed(WPARAM w, LPARAM l)////do this
{
	//WPARAM w is the nID (Control ID) of the Button we pressed

	CString s,str;
	m_cTab.GetDlgItem((int)w)->GetWindowText(s);
	str.Format("BUTTON %d was pressed [%s]",w,s);
	GetDlgItem(IDC_STATIC1)->SetWindowText(str);
	//TRACE("BUTTON %d was pressed [%s]\n",w,s);
	
	return 0;
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CTabExampleDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CTabExampleDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}
