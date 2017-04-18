// udptestDlg.cpp : implementation file
//

#include "stdafx.h"
#include "udptest.h"
#include "udptestDlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

#define	BUFFER_LEN 8192
unsigned char RcvBuffer[BUFFER_LEN];
unsigned int port;
int m_rcvport=5000;

CString GetLocalIP(int ipIndex)
{
	//获取版本和本机IP地址 获取本机第ipIndex个IP地址
	char r_iplist[16][256];
	int i=0;
	
	WORD wVersionRequested;
	WSADATA wsaData;
	char name[255];
	PHOSTENT hostinfo;
	wVersionRequested = MAKEWORD( 2, 0 );
	if ( WSAStartup( wVersionRequested, &wsaData ) == 0 )
	{
		if( gethostname ( name, sizeof(name)) == 0)
		{
			if((hostinfo = gethostbyname(name)) != NULL)
			{
				
				for (i=0;i<16; i++ )
				{
					_tcscpy(r_iplist[i], inet_ntoa( *(IN_ADDR*)hostinfo->h_addr_list[i] ));
					if ( hostinfo->h_addr_list[i] + hostinfo->h_length >= hostinfo->h_name )
						break;
				}
				//ip = inet_ntoa (*(struct in_addr *)*hostinfo->h_addr_list);
			}
		}
		WSACleanup();
	}
	return r_iplist[ipIndex];
}
/////////////////////////////////////////////////////////////////////////////
// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// No message handlers
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CUdptestDlg dialog

CUdptestDlg::CUdptestDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CUdptestDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CUdptestDlg)
		// NOTE: the ClassWizard will add member initialization here
	//}}AFX_DATA_INIT
	// Note that LoadIcon does not require a subsequent DestroyIcon in Win32
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CUdptestDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CUdptestDlg)
		// NOTE: the ClassWizard will add DDX and DDV calls here
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CUdptestDlg, CDialog)
	//{{AFX_MSG_MAP(CUdptestDlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_BUTTON1, OnButton1)
	ON_WM_TIMER()
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CUdptestDlg message handlers

BOOL CUdptestDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon
	
	// TODO: Add extra initialization here
	//CIPAddressCtrl* pWnd=(CIPAddressCtrl*)GetDlgItem(IDC_IPADDRESS1);
	//pWnd->SetWindowText("127.0.0.1");
	CString strIP=GetLocalIP(0);
	SetDlgItemText(IDC_IPADDRESS1,strIP);

	m_MySocket=new MySocket(this);
	m_MySocket->Create(m_rcvport,SOCK_DGRAM);

	SetTimer(100,200,0);
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CUdptestDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CUdptestDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

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

// The system calls this to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CUdptestDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CUdptestDlg::OnReceive(MySocket *psock)
{
	int datalength;
	CString SAddress;
	datalength=psock->ReceiveFrom(RcvBuffer,BUFFER_LEN,SAddress,port,0);//接收UDP传输数据
}

BOOL CUdptestDlg::DestroyWindow() 
{
	// TODO: Add your specialized code here and/or call the base class
	
	delete m_MySocket;
	return CDialog::DestroyWindow();
}

void CUdptestDlg::OnButton1() 
{
	// TODO: Add your control notification handler code here
	CString strIP;
	GetDlgItemText(IDC_IPADDRESS1,strIP);
	char Buffer[256];
	Buffer[0]=0x55;
	Buffer[1]=0xAA;
	m_MySocket->SendTo(Buffer,2,5000,strIP,0);//发送数据
}

void CUdptestDlg::OnTimer(UINT nIDEvent) 
{
	// TODO: Add your message handler code here and/or call default
	//刷新实时数据显示
	CString strTemp;
	strTemp.Format("%02x %02x %02x %02x %02x %02x %02x %02x",RcvBuffer[0],RcvBuffer[1],RcvBuffer[2],RcvBuffer[3],RcvBuffer[4],RcvBuffer[5],RcvBuffer[6],RcvBuffer[7]);
	strTemp.MakeUpper();
	SetDlgItemText(IDC_EDIT1,strTemp);
	CDialog::OnTimer(nIDEvent);
}
