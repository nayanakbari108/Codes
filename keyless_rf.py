def encrypt(str1,key):
    arr = []
    for i in range(key):
        row = ["0"]*len(str1)
        arr.append(row)

    j = 0 
    i = 0
    toggle = 0

    while(j<len(str1)):
        print(i,j)
        arr[i][j] = str1[j]
        j += 1
        if (toggle == 0 and i != key-1):
                i += 1
        elif(toggle == 0 and i == key-1):
            toggle = 1
            i -= 1
        elif (toggle == 1 and i != 0):
             i -= 1
        elif (toggle ==1 and i == 0):
             i += 1
             toggle =0
    for i in range(key):
        print(arr[i])
    cipherText = ""
    for i in range(key):
        cipherText += "".join(arr[i]).replace("0", "")
    return cipherText


str1 = input("Enter the string : ")
row = int(input("enter the row : "))
cipherText = encrypt(str1,row)
print(cipherText)
# plainText = decrypt(cipherText,key)
# print(plainText)