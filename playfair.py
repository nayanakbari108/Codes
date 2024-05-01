def refineStr(str1):
    str1.replace("j","i")
    strList = [x for x in str1]
    i = 0
    while(i < len(strList)-1):
        if (strList[i]==strList[i+1]):
            strList.insert(i+1,'x')
        i+=1
    listStr = "".join(strList)                                         
    if len(listStr)% 2 == 1:
        listStr += 'x'
    return listStr


def encrypt(str1,key):
    dict1 = {}
    key.replace("j","i")
    key1 = "".join(sorted(set(key),key=key.index))
    arr = []
    alphabets = "abcdefghiklmnopqrstuvwxyz"
    matrixAlpha = key1 +''.join(sorted(set(alphabets) - set(key1)))
    for i in range(0,25 ,5):
        arr.append([x for x in matrixAlpha[i : i+5]])
    print(arr)

   
    cipherText = ""
    for i in range(5):
        for j in range(5):
            dict1[arr[i][j]] = [i,j]
   
    for i in range(0,len(str1)-1,2):
        print(str1[i],str1[i+1])
        pos1 = dict1[str1[i]]     
        pos2 = dict1[str1[i+1]]
        
        if (pos1[0]== pos2[0]):
           cipherText += arr[pos1[0]][(pos1[1]+1)%5] + arr[pos2[0]][(pos2[1]+1)%5]
           
        elif (pos1[1]== pos2[1]):
           cipherText += arr[(pos1[0]+1)%5][pos1[1]] + arr[(pos2[0]+1)%5][pos2[1]]
          
        else:
            cipherText += arr[pos1[0]][pos2[1]] + arr[pos2[0]][pos1[1]]
            
    return cipherText

str1 = input("Enter the string : ")
key = input("enter the key : ")
str2 = refineStr(str1)
cipherText = encrypt(str2,key)
print(cipherText)
# plainText = decrypt(cipherText,key1)
# print(plainText)