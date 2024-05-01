def encrypt(str1,a,b):
    str2 = ""
    for i in str1:
        if i == " ":
            str2 += i
        else:
            if(i.islower()):
                str2 += chr((((ord(i)-97)*a + b) % 26) + 97) 
            else :
                str2 += chr((((ord(i)-ord("A"))*a + b) %26) +ord("A")) 
 
    return str2

def affine(val,a,b):
    if (val<= b):
        val = val + 26 - b
    else:
        val = val - b
    while(val % a != 0):
        val = val + 26
        # print("val is :",val)
    return val // a
        


def decrypt(str1,a,b):
    print(str1)
    str2 = ""
    for i in str1:
        if i == " ":
            str2 += i
        else:
            if(i.islower()):
                str2 += chr((affine(ord(i)-97,a,b) %26) + 97) 
            else :
                str2 += chr((affine(ord(i) -ord("A"),a,b) %26) + ord("A") )  
 
    return str2


str1 = input("Enter the string : ")
a = int(input("enter the a : "))
b = int(input("enter the b : "))
cipherText = encrypt(str1,a,b)
print(cipherText)

plainText = decrypt(cipherText,a,b)
print(plainText)

