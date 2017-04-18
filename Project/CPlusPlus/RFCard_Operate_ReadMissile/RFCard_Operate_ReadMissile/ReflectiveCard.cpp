/**************************************************/
/**************************************************/
/************RFM2g头文件及宏定义******************/
/**************************************************/
/**************************************************/
#if (defined(WIN32))
#include "rfm2g_windows.h"
#endif

#include <stdio.h>
#include <string.h>
#include "rfm2g_api.h"
#include <time.h>
#include "ReflectiveCard.h"
#if (defined(RFM2G_LINUX))

#ifdef CONFIG_DEVFS_FS
#define DEVICE_PREFIX   "/dev/rfm2g/"
#else
#define DEVICE_PREFIX   "/dev/rfm2g"
#endif

#define PROCFILE         "/proc/rfm2g"

#elif defined(RFM2G_VXWORKS)

#define DEVICE_PREFIX   "RFM2G_"

#elif defined(SOLARIS)

#define DEVICE_PREFIX   "/dev/rfm2g"

#elif defined(WIN32)

#define DEVICE_PREFIX   "\\\\.\\rfm2g"
#else

#error Please define DEVICE_PREFIX for your driver
#endif

#define RFCARD_TRANS_MODE_ADDR 0x0010  //反射内存卡主控传输标志信息存储地址
#define START_ADDRESS   0x0000
#define OFFSET_1        0x3000//读取反射内存卡偏移地址
#define OFFSET_2        0x4000//写入反射内存卡偏移地址
/**************************************************/
/**************************************************/
/****************RFM2g头文件及宏定义结束*********/
/**************************************************/
/**************************************************/
enum MainControlMode//主控传输标志信息
{
	RF_Query_MissData = 1,//反射内存卡查询模式传输弹道数据
	RF_Break_MissData,//反射内存卡中断模式传输弹道数据
	UDP,//数据库用到
	SYS_Init,//反射内存卡——系统初始化
	Reboot,//重启VxWorks系统
	PRF_Start,
	PRF_Stop,
	Last
};
enum  MainControlMode static MainCtrolMode = RF_Break_MissData;

#define TIMEOUT         60000   //单位为ms

int RFM_Card_Operate::RFM_Card_Init(rfm2gEventType EventType)//反射内存卡初始化函数，初始化Handle句柄等参数
{
	RFM2G_STATUS result;
	/* Open the Reflective Memory device */
	sprintf(device, "%s%d", DEVICE_PREFIX, numDevice);
	result = RFM2gOpen(device, &Handle);
	if (result != RFM2G_SUCCESS)
	{
		printf("ERROR: RFM2gOpen() failed.\n");
		printf("Error: %s.\n\n", RFM2gErrorMsg(result));
		return(-1);
	}
	/*获取反射内存卡的型号以及内存大小信息*/
	result = RFM2gGetConfig(Handle, &config);
	if (result == RFM2G_SUCCESS)
	{
		printf("\nNode ID is %d\n", config.NodeId);
		printf("The total memory size of %s is %d MBytes\n", config.Device, config.MemorySize / 1048576);
		printf("The memory offset range is 0x00000000~0x10000000\n");
	}
	else
	{
		printf("ERROR: RFM2gGetConfig() failed.\n");
		printf("Error: %s.\n\n", RFM2gErrorMsg(result));
		return(-1);
	}
	/*设置大小端，使不能字节反转*/
	result_ByteSwap = RFM2gSetPIOByteSwap(Handle, RFM2G_FALSE);
	if (result_ByteSwap != RFM2G_SUCCESS)/*设置大小端失败*/
	{
		printf("ERROR: RFM2gSetPIOByteSwap() failed.\n");
		printf("Error: %s.\n\n", RFM2gErrorMsg(result_ByteSwap));
		return(-1);
	}
	result_ByteSwap = RFM2gGetPIOByteSwap(Handle, &byteSwap);
	if (result_ByteSwap != RFM2G_SUCCESS)/*获取大小端设置状态失败*/
	{
		printf("ERROR: RFM2gGetPIOByteSwap() failed.\n");
		printf("Error: %s.\n\n", RFM2gErrorMsg(result_ByteSwap));
		return(-1);
	}
	else/*获取大小端设置状态成功*/
	{
		if (byteSwap == RFM2G_TRUE)
		{
			printf("The byte swapping of PIO transfers to an RFM2g device is enabled!\n");
		}
		else
		{
			printf("The byte swapping of PIO transfers to an RFM2g device is Disabled!\n");
		}
	}
	//写传输模式标志位
	int temp = (int)MainCtrolMode;
	result = RFM2gWrite(Handle, RFCARD_TRANS_MODE_ADDR, (void *)&temp, sizeof(int));//往地址RFCARD_TRANS_MODE_ADDR写入当前反射内存卡传输模式参数
	if (result != RFM2G_SUCCESS)
	{
		printf("Error: %s\n", RFM2gErrorMsg(result));
		RFM2gClose(&Handle);
		return(-1);
	}
	RFM_Card_EnableEvent(EventType);//使能RFM2GEVENT_INTR2中断

}
RFM2G_STATUS RFM_Card_Operate::RFM_Card_EnableEvent(rfm2gEventType EventType)
{
	/* Now wait on an interrupt from the other Reflective Memory board */
	EventInfo_Receive.Event = EventType;  /* We'll wait on this interrupt */
	EventInfo_Receive.Timeout = TIMEOUT;       /* We'll wait this many milliseconds */
	RFM2G_STATUS result = RFM2gEnableEvent(Handle, EventType);//使能接收的中断类型RFM2GEVENT_INTR2
	if (result != RFM2G_SUCCESS)
	{
		printf("Error: %s\n", RFM2gErrorMsg(result));
		RFM2gClose(&Handle);
		return(result);
	}
}
RFM2G_STATUS RFM_Card_Operate::RFM_Card_DisableEvent()
{
	//关闭中断
	RFM2G_STATUS result = RFM2gDisableEvent(Handle, EventInfo_Receive.Event);
	return result;

}


RFM2G_STATUS RFM_Card_Operate::RFM_Write_Missle(struct MissilePosInfo outbuffer, rfm2gEventType EventType)
{
	RFM2G_STATUS result = RFM2gWrite(Handle, OFFSET_WRT, (void *)&outbuffer, sizeof(struct  MissilePosInfo));
	/* Send an interrupt to the other Reflective Memory board */
	result = RFM2gSendEvent(Handle, OhterNodeID, EventType, 0);
	Sleep(2);//延时极其重要，不然会出错，导致第一次接收的是上一次的最后一个弹道数据
	return result;
}

RFM2G_STATUS RFM_Card_Operate::WaitForEvent()
{
	RFM2G_STATUS result = RFM2gWaitForEvent(Handle, &EventInfo_Receive);
	/* Got the interrupt, see who sent it */
	OhterNodeID = EventInfo_Receive.NodeId;
	return result;
}

RFM2G_STATUS RFM_Card_Operate::RFM_Read_Missle(struct MissilePosInfo &inbuffer)
{
	RFM2G_STATUS result = RFM2gRead(Handle, OFFSET_RD, (void *)&inbuffer, sizeof(struct  MissilePosInfo));
	return result;
}

RFM_Card_Operate::~RFM_Card_Operate()//反射内存卡初始化函数，初始化Handle句柄等参数
{
	//Disable中断
	RFM_Card_DisableEvent();
	//关闭反射内存卡
	RFM2gClose(&Handle);
}


// 判断弹道结构体数据是否相等
int RFM_Card_Operate::StructCMP(struct MissilePosInfo Para1, struct MissilePosInfo Para2)
{
#ifdef DEBUG_MissStruct80Bytes   //采用80Bytes的弹道结构体
	if (Para1.CurrentTime == Para2.CurrentTime &&
		Para1.Position[0] == Para2.Position[0] &&
		Para1.Position[1] == Para2.Position[1] &&
		Para1.Position[2] == Para2.Position[2] &&
		Para1.Velocity[0] == Para2.Velocity[0] &&
		Para1.Velocity[1] == Para2.Velocity[1] &&
		Para1.Velocity[2] == Para2.Velocity[2] &&
		Para1.Acceleration[0] == Para2.Acceleration[0] &&
		Para1.Acceleration[1] == Para2.Acceleration[1] &&
		Para1.Acceleration[2] == Para2.Acceleration[2] &&
		Para1.theta == Para2.theta &&
		Para1.psi == Para2.psi &&
		Para1.gamma == Para2.gamma &&
		Para1.sOmegaX1 == Para2.sOmegaX1 &&
		Para1.sOmegaY1 == Para2.sOmegaY1 &&
		Para1.sOmegaZ1 == Para2.sOmegaZ1 &&
		Para1.sTheta == Para2.sTheta &&
		Para1.sAlpha == Para2.sAlpha &&
		Para1.sSigma == Para2.sSigma &&
		Para1.counter == Para2.counter
		)//结构体相等返回1
		return 1;
	else//结构体不相等返回0
		return 0;
#elif defined DEBUG_MissStruct520Bytes  //采用520Bytes的弹道结构体
	if ((fabs(Para1.CurrentTime - Para2.CurrentTime) < 0.0000001) &&
		(fabs(Para1.Position[0] - Para2.Position[0]) < 0.0000001) &&
		(fabs(Para1.Position[1] - Para2.Position[1]) < 0.0000001) &&
		(fabs(Para1.Position[2] - Para2.Position[2]) < 0.0000001) &&
		(fabs(Para1.Velocity[0] - Para2.Velocity[0]) < 0.0000001) &&
		(fabs(Para1.Velocity[1] - Para2.Velocity[1]) < 0.0000001) &&
		(fabs(Para1.Velocity[2] - Para2.Velocity[2]) < 0.0000001) &&
		(fabs(Para1.Acceleration[0] - Para2.Acceleration[0]) < 0.0000001) &&
		(fabs(Para1.Acceleration[1] - Para2.Acceleration[1]) < 0.0000001) &&
		(fabs(Para1.Acceleration[2] - Para2.Acceleration[2]) < 0.0000001) &&
		(fabs(Para1.theta - Para2.theta) < 0.0000001) &&
		(fabs(Para1.psi - Para2.psi) < 0.0000001) &&
		(fabs(Para1.gamma - Para2.gamma) < 0.0000001) &&
		(fabs(Para1.sOmegaX1 - Para2.sOmegaX1) < 0.0000001) &&
		(fabs(Para1.sOmegaY1 - Para2.sOmegaY1) < 0.0000001) &&
		(fabs(Para1.sOmegaZ1 - Para2.sOmegaZ1) < 0.0000001) &&
		(fabs(Para1.sTheta - Para2.sTheta) < 0.0000001) &&
		(fabs(Para1.sAlpha - Para2.sAlpha) < 0.0000001) &&
		(fabs(Para1.sSigma - Para2.sSigma) < 0.0000001) &&
		(fabs(Para1.uiWaveWid - Para2.uiWaveWid) < 0.0000001) &&
		(fabs(Para1.uiApcHight - Para2.uiApcHight) < 0.0000001) &&
		(memcmp(Para1.Rsvd, Para2.Rsvd, sizeof(short) * (256 - 42)) == 0) &&//比较int数组是否相等
		(Para1.usDataFlag == Para2.usDataFlag) &&
		(Para1.usDataValid == Para2.usDataValid) &&
		(Para1.counter == Para2.counter) &&
		(Para1.usSumCheck == Para2.usSumCheck)
		)//结构体相等返回1
		return 1;
	else//结构体不相等返回0
		return 0;
#endif
}

