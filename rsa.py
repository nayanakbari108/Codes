print("Enter 2 large prime numbers:")
p = int(input(" p :"))
q = int(input(" q :"))

n = p*q
print("Thus value of n is : ",n)

phiOfN = (p-1)*(q-1)
print("Thus Phi(n) is :",phiOfN)

e = int(input("enter the public key :"))
if (e>1 and e<phiOfN and phiOfN % e != 0):
    print("Valid Public key as between 1 and phi(n) and not a factor of phi(n)")
    k = 0
    while((k * phiOfN + 1)%e != 0):
        k +=1
    d = (k * phiOfN + 1)//e
    print("value of private key is :",d)

    plainText =int(input("input plainText :"))
    cipherText = plainText**e % n
    print("cipherText :",cipherText)

    cText =int(input("input cipherText :"))
    pText = cText**d % n
    print("plainText :",pText)


else :
    print("invalid public key")
