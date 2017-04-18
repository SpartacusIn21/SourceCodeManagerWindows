UINT32 Dec2Hex(CString addr_dec)//将输入的10进制转换成对应的十六进制，如输入1000转换成0x1000
{
	std::map <CString, UINT32> Hex2Dec_map;//map
	CString hexstr[16] = {_TEXT("0"), _TEXT("1"), _TEXT("2"), _TEXT("3"),_TEXT("4"),_TEXT("5"),_TEXT("6"),_TEXT("7"),_TEXT("8"),_TEXT("9"),_TEXT("a"),_TEXT("b"),_TEXT("c"),_TEXT("d"),_TEXT("e"), _TEXT("f")};
	CString hexstr_others[6] = {_TEXT("A"),_TEXT("B"),_TEXT("C"),_TEXT("D"),_TEXT("E"), _TEXT("F")};
	for(int i = 0; i < 16; i++){
		Hex2Dec_map.insert(std::make_pair(hexstr[i], i));
	}
	for(int i  = 0; i < 6; i++){
		Hex2Dec_map.insert(std::make_pair(hexstr_others[i], i+10));
	}
	CString str_addr_dec = addr_dec;
	char RlCardMaxAddr_char[20];
	UINT32 temp_hex = 0;
	int Bits = addr_dec.GetLength();
	int count = Bits;
	for(int i = 0; i < Bits; i++)
	{
		/*temp_hex += temp_dec / (UINT32)(pow(10.0, Bits-1)) * (UINT32)pow(16.0, Bits-1);
		temp_dec -= (UINT32)(pow(10.0, Bits-1));*/
		temp_hex += Hex2Dec_map[CString(addr_dec[i])] * (UINT32)pow(16.0, --count);
	}
	return temp_hex;
}