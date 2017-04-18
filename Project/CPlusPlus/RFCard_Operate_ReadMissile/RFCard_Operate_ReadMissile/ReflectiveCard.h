#pragma once
#if (defined(WIN32))
#include "rfm2g_windows.h"
#endif
#include "rfm2g_api.h"
#include <iostream>
using namespace std;
void RFM_Break();
//#define DEBUG_MissStruct80Bytes    //弹道结构体为80Bytes
#define DEBUG_MissStruct520Bytes    //弹道结构体为520Bytes
#ifdef DEBUG_MissStruct80Bytes  //弹道结构体为80Bytes
struct  MissilePosInfo//弹道坐标位置信息结构体，占用80Bytes，得修改为占用520Bytes的结构体格式
{
	float CurrentTime;//弹道位置对应方位向时刻
	float Position[3];//弹道坐标位置
	float Velocity[3];//导弹在该弹道位置处三个速度分量
	float Acceleration[3];//导弹在该弹道位置处三个加速度分量
	float theta;
	float psi;
	float gamma;
	float sOmegaX1;
	float sOmegaY1;
	float sOmegaZ1;
	float sTheta;
	float sSigma;
	float sAlpha;
	int counter;//当前弹道时刻的方位点数
};
#elif defined DEBUG_MissStruct520Bytes   //弹道结构体为520Bytes
struct  MissilePosInfo//弹道坐标位置信息结构体，占用80Bytes，得修改为占用520Bytes的结构体格式
{
	float CurrentTime;//弹道位置对应方位向时刻
	float Position[3];//弹道坐标位置
	float Velocity[3];//导弹在该弹道位置处三个速度分量
	float Acceleration[3];//导弹在该弹道位置处三个加速度分量
	float theta;
	float psi;
	float gamma;
	float sOmegaX1;
	float sOmegaY1;
	float sOmegaZ1;
	float sTheta;
	float sSigma;
	float sAlpha;
	float  uiWaveWid;              // 波门
	float  uiApcHight;             // 预定成像高度,short占用两个字节，int占用4个字节
	short  Rsvd[214];           // 保留字
	short   usDataFlag;             // 参数标志字
	short   usDataValid;            // 数据有效标志
	short   counter;					//当前弹道时刻的方位点数// 参数更新计数 
	short   usSumCheck;             // 参数校验
};
#else 
printf("Debug Macro is wrong!\n");
#endif
class RFM_Card_Operate{
private:
	RFM2G_BOOL 	   byteSwap;			/*获取大小端设置状态，为RFM2G_TRUE或RFM2G_FALSE*/
	STDRFM2GCALL   result_ByteSwap;     /*大小端设置返回值*/
	RFM2GEVENTINFO EventInfo_Receive;              /* Info about received interrupts    */
	UINT OFFSET_WRT = 0x4000;//反射内存卡写地址——默认为0x3000
	UINT OFFSET_RD = 0x3000;//反射内存卡读地址——默认为0x4000
	

protected:

public:
	//反射内存卡公用参数变量
	RFM2G_INT32 numDevice;
	RFM2G_NODE     OhterNodeID;             /* OhterNodeID*/
	char     device[40];             /* Name of PCI RFM2G device to use   */
	RFM2GHANDLE    Handle = 0;//反射内存卡句柄，非常重要
	RFM2GCONFIG    config;					/*获取RFM2g配置结构*/
	
	//反射内存卡公用函数
	RFM_Card_Operate(RFM2G_INT32 numDevice_Para, RFM2G_NODE OhterNodeID_Para) :numDevice(numDevice_Para), OhterNodeID(OhterNodeID_Para){};
	int RFM_Card_Init(rfm2gEventType EventType);//反射内存卡初始化
	RFM2G_STATUS RFM_Card_EnableEvent(rfm2gEventType EventType);//Enable中断
	RFM2G_STATUS RFM_Card_DisableEvent();//Disable中断
	RFM2G_STATUS WaitForEvent();
	RFM2G_STATUS RFM_Write_Missle(struct MissilePosInfo outbuffer,rfm2gEventType EventType);
	RFM2G_STATUS RFM_Read_Missle(struct MissilePosInfo &inbuffer);
	int StructCMP(struct MissilePosInfo Para1, struct MissilePosInfo Para2);//对比结构体大小
	~RFM_Card_Operate();


};

