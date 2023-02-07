num1 = 233
num2 = 499
num3 = 8

def decimalToBinary(decimal, res):

    if decimal == 0:
        return res 

    res = str(decimal % 2) + res 
    
    return decimalToBinary(decimal // 2, res)


print(decimalToBinary(num1, ""))
print(decimalToBinary(num2, ""))
print(decimalToBinary(num3, ""))