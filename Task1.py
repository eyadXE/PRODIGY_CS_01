def encrypt(word,skey):
    newword=""

    for k in range(len(word)):
        if(chr(ord(word[k])+skey).isalpha()):
             num=ord(word[k])
             if(word[k]=='z'or word[k]=='Z' ):
                 num=ord(word[k])-26
             newletter=chr(num+skey)
             #newletter+=1
             newword+=(newletter)
        else:
            num = ord(word[k]) - 26
            newletter = chr(num + skey)
            newword += (newletter)

    return newword

def decrypt(word, skey):
    newword = ""

    for k in range(len(word)):
        if(chr(ord(word[k])-skey).isalpha()):
            num = ord(word[k])
            if (word[k] == 'a' or word[k] == 'A'):
               num = ord(word[k]) + 26
            newletter = chr(num - skey)
            newword += (newletter)
        else:
            num = ord(word[k]) + 26
            newletter = chr(num - skey)
            newword += (newletter)


    return newword


z=True
print("Entre the type of conversion you want to make (encryption=1,decryption=0)")
while(z):
    type=int(input())
    if(type==0 or type==1):
        z=False
    else:
        print("please choose form the options")
print("Entre the shift key")
p=0
try:
    x=int(input())
    p=1
except:
    print('wrong input')
if(p==1):
    print("Entre the word ")
    try:
        y=input()
    except:
        print("wrong input")
    if(type==1):
        print(encrypt(y, x))
        #print("\n")
    else:
        print(decrypt(y, x))

