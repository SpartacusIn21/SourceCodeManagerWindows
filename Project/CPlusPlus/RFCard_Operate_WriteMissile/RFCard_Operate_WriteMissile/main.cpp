// VisualSimulation_RFcardMissleRecv.cpp: 主项目文件。

#include "stdafx.h"
#include "ReflectiveCard.h"
using namespace System;
int main(array<System::String ^> ^args)
{
/*********************反射内存卡写弹道数据使用示例*********************/
	//反射内存卡读写数据变量
	RFM_Card_Operate RFCardMissOperate(1, 4);//其中1为Device ID——即本地反射内存卡的设备ID，4为接收方Node ID
	int result_RFM_CardInit = RFCardMissOperate.RFM_Card_Init(RFM2GEVENT_INTR2);//RFM2GEVENT_INTR2是本地反射内存卡接收中断类型
	if (result_RFM_CardInit == -1)
	{
		printf("反射内存卡初始化错误！\n");
		return -1;
	}
	int Miss_Transfer_CheckNums = 0;//反射内存卡传输正确点数
	struct MissilePosInfo outbuffer;
	struct MissilePosInfo inbuffer;
	memset(&outbuffer, 0, sizeof(struct MissilePosInfo));
	memset(&inbuffer, 0, sizeof(struct MissilePosInfo));


	//循环开始
	//生成弹道数据并赋值给outbuffer
	//...
	//写反射内存卡
	//将弹道数据写入反射内存卡
	RFM2G_STATUS result_Write = RFCardMissOperate.RFM_Write_Missle(outbuffer, RFM2GEVENT_INTR1);//RFM2GEVENT_INTR1是远端反射内存卡接收中断类型
	if (result_Write != RFM2G_SUCCESS)
	{
		return(-1);
	}
	else
	{
		RFM2G_STATUS result_Event = RFCardMissOperate.WaitForEvent();
		if (result_Event != RFM2G_SUCCESS)
		{
			return(-1);
		}
		else
		{
			RFM2G_STATUS result_Read = RFCardMissOperate.RFM_Read_Missle(inbuffer);
			if (result_Read != RFM2G_SUCCESS)
			{
				return(-1);
			}
			else
			{
				int Result_CMP = RFCardMissOperate.StructCMP(outbuffer, inbuffer);
				if (Result_CMP == 1)
				{
					Miss_Transfer_CheckNums++;
				}
			}
		}

	}
	//...
	//循环结束

/**************************************************************/
    return 0;
}
