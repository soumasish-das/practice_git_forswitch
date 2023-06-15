x="ABCd!@123"
vowel=('a','e','i','o','u','A','E','I','O','U')
special=('!','@','?')
number=("1","2","3","4","5","6","7","8","0","9")
print("total length of the string:"+str(len(x)))
count=0
count1=0
count2=0
count3=0
count4=0
for i in x:
    if i in vowel:
        count=count+1
    elif i in number:
        count4 = count4 + 1
    elif i in special:
        count1=count1+1
    elif (i==' '):
        count2=count2+1
    else:
        count3=count3+1
print("vowels are:" +str(count))
print("special are:" +str(count1))
print("spaces are:" +str(count2))
print("consonents are:" +str(count3))
print("numbers are:" +str(count4))