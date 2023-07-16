import random

sbox = [99, 124, 119, 123, 242, 107, 111, 197, 48, 1, 103, 43, 254,
    215, 171, 118, 202, 130, 201, 125, 250, 89, 71, 240, 173, 212, 
   	162, 175, 156, 164, 114, 192, 183, 253, 147, 38, 54, 63, 247, 204, 
   	52, 165, 229, 241, 113, 216, 49, 21, 4, 199, 35, 195, 24, 150, 5, 
   	154, 7, 18, 128, 226, 235, 39, 178, 117, 9, 131, 44, 26, 27, 110, 
   	90, 160, 82, 59, 214, 179, 41, 227, 47, 132, 83, 209, 0, 237, 32, 
   	252, 177, 91, 106, 203, 190, 57, 74, 76, 88, 207, 208, 239, 170, 
   	251, 67, 77, 51, 133, 69, 249, 2, 127, 80, 60, 159, 168, 81, 163, 
   	64, 143, 146, 157, 56, 245, 188, 182, 218, 33, 16, 255, 243, 210, 
	205, 12, 19, 236, 95, 151, 68, 23, 196, 167, 126, 61, 100, 93, 25, 
   	115, 96, 129, 79, 220, 34, 42, 144, 136, 70, 238, 184, 20, 222, 94,
	11, 219, 224, 50, 58, 10, 73, 6, 36, 92, 194, 211, 172, 98, 145, 
   	149, 228, 121, 231, 200, 55, 109, 141, 213, 78, 169, 108, 86, 244, 
   	234, 101, 122, 174, 8, 186, 120, 37, 46, 28, 166, 180, 198, 232, 
   	221, 116, 31, 75, 189, 139, 138, 112, 62, 181, 102, 72, 3, 246, 14,
    97, 53, 87, 185, 134, 193, 29, 158, 225, 248, 152, 17, 105, 217, 
   	142, 148, 155, 30, 135, 233, 206, 85, 40, 223, 140, 161, 137, 13, 
   	191, 230, 66, 104, 65, 153, 45, 15, 176, 84, 187, 22]

invSbox = [82, 9, 106, 213, 48, 54, 165, 56, 191, 64, 163, 158, 129, 243, 
	215, 251, 124, 227, 57, 130, 155, 47, 255, 135, 52, 142, 67, 68, 196, 222, 
	233, 203, 84, 123, 148, 50, 166, 194, 35, 61, 238, 76, 149, 11, 66, 250, 195, 
	78, 8, 46, 161, 102, 40, 217, 36, 178, 118, 91, 162, 73, 109, 139, 209, 37, 114, 
	248, 246, 100, 134, 104, 152, 22, 212, 164, 92, 204, 93, 101, 182, 146, 108, 112,
	 72, 80, 253, 237, 185, 218, 94, 21, 70, 87, 167, 141, 157, 132, 144, 216, 171,
	  0, 140, 188, 211, 10, 247, 228, 88, 5, 184, 179, 69, 6, 208, 44, 30, 143, 202, 
	  63, 15, 2, 193, 175, 189, 3, 1, 19, 138, 107, 58, 145, 17, 65, 79, 103, 220, 234, 
	  151, 242, 207, 206, 240, 180, 230, 115, 150, 172, 116, 34, 231, 173, 53, 133, 226,
	   249, 55, 232, 28, 117, 223, 110, 71, 241, 26, 113, 29, 41, 197, 137, 111, 183, 98,
    14, 170, 24, 190, 27, 252, 86, 62, 75, 198, 210, 121, 32, 154, 219, 192, 254, 120,
     205, 90, 244, 31, 221, 168, 51, 136, 7, 199, 49, 177, 18, 16, 89, 39, 128, 236, 
     95, 96, 81, 127, 169, 25, 181, 74, 13, 45, 229, 122, 159, 147, 201, 156, 239, 
     160, 224, 59, 77, 174, 42, 245, 176, 200, 235, 187, 60, 131, 83, 153, 97, 23, 43,
      4, 126, 186, 119, 214, 38, 225, 105, 20, 99, 85, 33, 12, 125]

mult2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 
	34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 
	68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 
	102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 
	130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 
	158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 
	186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 
	214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 
	242, 244, 246, 248, 250, 252, 254, 27, 25, 31, 29, 19, 17, 23, 21, 11, 
	9, 15, 13, 3, 1, 7, 5, 59, 57, 63, 61, 51, 49, 55, 53, 43, 41, 47, 45,
	35, 33, 39, 37, 91, 89, 95, 93, 83, 81, 87, 85, 75, 73, 79, 77, 67, 
	65, 71, 69, 123, 121, 127, 125, 115, 113, 119, 117, 107, 105, 111, 
	109, 99, 97, 103, 101, 155, 153, 159, 157, 147, 145, 151, 149, 139, 
	137, 143, 141, 131, 129, 135, 133, 187, 185, 191, 189, 179, 177, 183, 
	181, 171, 169, 175, 173, 163, 161, 167, 165, 219, 217, 223, 221, 211, 
	209, 215, 213, 203, 201, 207, 205, 195, 193, 199, 197, 251, 249, 255, 
	253, 243, 241, 247, 245, 235, 233, 239, 237, 227, 225, 231, 229]

def roundKey(index: int):
	if index <= 1:
		return 1
	temp = roundKey(index-1)
	return mult2[temp]

def rotate(arr: list):
	return [arr[1], arr[2], arr[3], arr[0]]

def sBox(num: int):
	return sbox[num]

def sBoxSub(arr: list):
	return [sBox(i) for i in arr]

def keyExpansion(initialKey: str):
	expandedKey = [ord(c) for c in initialKey]
	roundNum = 4
	tempArr = [0,0,0,0]
	while roundNum < 44:
		from4RoundsAgo = expandedKey[4*(roundNum-4):4*(roundNum-3)]
		prevRound = expandedKey[4*(roundNum-1):4*roundNum]
		if roundNum % 4 == 0:
			prevRound = sBoxSub(rotate(prevRound))
			for i in range(4):
				tempArr[i] = from4RoundsAgo[i]^prevRound[i]
			tempArr[0] = tempArr[0]^roundKey(roundNum//4)
		else:
			for i in range(4):
				tempArr[i] = from4RoundsAgo[i]^prevRound[i]
		expandedKey=expandedKey+tempArr
		roundNum += 1
	return [expandedKey[i:i+16] for i in range(0,len(expandedKey),16)]

def keyGen(length: int):
	key = ''
	for i in range(length):
		key = key + chr(random.randrange(0,255))
	return key

def AES128KeyGeneration():
	return keyGen(16)

def AES128Encryption(key: str, message: str, padding: bool=True):
	keys = keyExpansion(key)
	tempArr = strToInt(message)
	if padding:
		tempArr=pad(tempArr)

	for i in range(len(
		tempArr
	)):
		block = tempArr[i]
		block= XOR(block, keys[0])
		for j in range(1,10):
			block=AESEncRound(keys[j],block)
		block=AESEncLastRound(
			keys[10]
				,
			block
				)
		tempArr[i]=block
	return intToStr(tempArr)

def AES128Decryption(key: str, ct: str, padding: bool=True):
	keys = keyExpansion(key)
	tempArr = strToInt(ct)
	
	for i in range(len(tempArr)):
		block = tempArr[i]
		block = XOR(block, keys[10])
		for j in range(9,0,-1):
			block=AESDecRound(keys[j],block)
		block=AESDecFirstRound(keys[0],block)
		tempArr[i]=block
	
	if padding:
		tempArr = unpad(tempArr)
	
	return intToStr(tempArr)

def AESEncRound(key: str, block: list):
	tempMat = subBytes(block)
	tempMat = shiftRows(tempMat)
	tempMat = mixCols(tempMat)
	return XOR(tempMat, key)

def AESEncLastRound(key: str, block: list):
	tempMat = subBytes(block)
	tempMat = shiftRows(tempMat)
	return XOR(tempMat, key)

def AESDecRound(key: str, block: list):
    tempMat = invShiftRows(block)
    tempMat = invSubBytes(tempMat)
    tempMat = XOR(tempMat, key)
    tempMat = invMixCols(tempMat)
    return tempMat

def AESDecFirstRound(key: str, block: list):
    tempMat = invShiftRows(block)
    tempMat = invSubBytes(tempMat)
    tempMat = XOR(tempMat, key)
    return tempMat

def XOR(m1: list, m2: list):
	res = [0 for i in range(16)]
	for i in range(16):
		res[i] = m1[i]^m2[i]
	return res

def strToInt(s: str):
	res = [ord(c) for c in s]
	return [res[i:i+16] for i in range(0, len(res),16)]

def intToStr(i_arr: int):
	res = ''
	for i in i_arr:
		for byte in i:
			res = res + chr(byte)
	return res

def pad(blocks: list):
	tempArr = [i for i in blocks]
	lastIndex = len(blocks)-1
	lastBlockSize = len(blocks[lastIndex])
	if lastBlockSize < 16:
		tempArr[lastIndex] = tempArr[lastIndex]+[16-lastBlockSize for i in range(16-lastBlockSize)]
	else:
		tempArr = tempArr + [[16 for i in range(16)]]
	return tempArr

def unpad(blocks: list):
	tempArr = [i for i in blocks]
	lastIndex = len(blocks)-1
	padLength = blocks[lastIndex][15]
	if padLength == 16:
		return tempArr[0:lastIndex]
	else:
		tempArr[lastIndex]=tempArr[lastIndex][0:16-padLength]
		return tempArr

def subBytes(arr: list):
	return [sbox[byte] for byte in arr]

def invSubBytes(arr: list):
	return [invSbox[int(byte)] for byte in arr]

def shiftRows(arr: list):
	temp_array = arr[0:16]
	temp_row = []
	for j in range(1,4):
		for i in range(j,4):
			temp_row = temp_array[4*i:4*i+4]
			temp_row.append(temp_row.pop(0))
			temp_array[4*i:4*i+4] = temp_row
	return temp_array

def invShiftRows(arr: list):
	temp_array = arr[0:16]
	temp_row = []
	for j in range(1,4):
		for i in range(j,4):
			temp_row = temp_array[4*i:4*i+4]
			temp_row.insert(0,temp_row.pop(-1))
			temp_array[4*i:4*i+4] = temp_row
	return temp_array

def mixCols(arr: list):
	tempArr = [0 for i in arr]
	for i in range(4):
		tempCol=[arr[i],arr[4+i],arr[8+i],arr[12+i]]
		tempCol= mixCol(tempCol)
		tempArr[i]=tempCol[0]
		tempArr[4+i]=tempCol[1]
		tempArr[8+i]=tempCol[2]
		tempArr[12+i]=tempCol[3]
	return tempArr

def mixCol(arr: list):
	tempCol = [0,0,0,0]
	tempCol[0] = GaloisMultiply(2, arr[0]) ^ GaloisMultiply(3, arr[1]) ^ arr[2] ^ arr[3]
	tempCol[1] = arr[0] ^ GaloisMultiply(2, arr[1]) ^ GaloisMultiply(3, arr[2]) ^ arr[3]
	tempCol[2] = arr[0] ^ arr[1] ^ GaloisMultiply(2, arr[2]) ^ GaloisMultiply(3, arr[3])
	tempCol[3] = GaloisMultiply(3, arr[0]) ^ arr[1] ^ arr[2] ^ GaloisMultiply(2, arr[3])
	return tempCol

def invMixCols(arr: list):
	tempArr = [0 for i in arr]
	for i in range(0,4):
		tempCol=[arr[i],arr[4+i],arr[8+i],arr[12+i]]
		tempCol= invMixCol(tempCol)
		tempArr[i]=tempCol[0]
		tempArr[4+i]=tempCol[1]
		tempArr[8+i]=tempCol[2]
		tempArr[12+i]=tempCol[3]
	return tempArr

def invMixCol(arr: list):
	tempCol = [0,0,0,0]
	tempCol[0] = GaloisMultiply(14, arr[0]) ^ GaloisMultiply(11, arr[1]) ^ GaloisMultiply(13, arr[2]) ^ GaloisMultiply(9, arr[3])
	tempCol[1] = GaloisMultiply(9, arr[0]) ^ GaloisMultiply(14, arr[1]) ^ GaloisMultiply(11, arr[2]) ^ GaloisMultiply(13, arr[3])
	tempCol[2] = GaloisMultiply(13, arr[0]) ^ GaloisMultiply(9, arr[1]) ^ GaloisMultiply(14, arr[2]) ^ GaloisMultiply(11, arr[3])
	tempCol[3] = GaloisMultiply(11, arr[0]) ^ GaloisMultiply(13, arr[1]) ^ GaloisMultiply(9, arr[2]) ^ GaloisMultiply(14, arr[3])
	return tempCol

def GaloisMultiply(i: int, x: int):
	if i == 1:
		return x
	elif i == 2 and x >= 128:
		return (2*x)^283
	elif i == 2 and x < 128:
		return 2*x
	elif i == 3:
		return x^GaloisMultiply(2,x)
	elif i == 4:
		return GaloisMultiply(2,GaloisMultiply(2,x))
	elif i == 5:
		return x^GaloisMultiply(4,x)
	elif i == 6:
		return GaloisMultiply(2, GaloisMultiply(3,x))
	elif i == 7:
		return x^GaloisMultiply(6,x)
	elif i == 8:
		return GaloisMultiply(2, GaloisMultiply(2, GaloisMultiply(2, x)))
	elif i == 9:
		return x^GaloisMultiply(8, x)
	elif i == 10:
		return GaloisMultiply(2, GaloisMultiply(5, x))
	elif i == 11:
		return x^GaloisMultiply(10, x)
	elif i == 12:
		return GaloisMultiply(2, GaloisMultiply(6, x))
	elif i == 13:
		return x^GaloisMultiply(12, x)
	elif i == 14:
		return GaloisMultiply(2, GaloisMultiply(7, x))
	else: return None