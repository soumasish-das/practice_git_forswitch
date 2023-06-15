string="helloiau"
vowel=('a','e','i','o','u','A','E','I','O','U')
list=[]
string1=""
for i in string:
    if i in vowel:
        list.append(i)
#print(list)
t=0
for i in range(0,len(list),2):
    if (len(list)>i+1):
        #print(list[i])
        t=list[i]
        list[i]=list[i+1]
        list[i+1]=t
#print(list)
count=0
for i in string:
    if i not in vowel:
        string1=string1+i
    else:
        string1=string1+list[count]
        count=count+1

print(string1)


