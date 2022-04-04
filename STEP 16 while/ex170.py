a= int(input("first num :"))
b= int(input("second num :"))
if b<a :
    tmp=a
    a=b
    b=tmp

tmp =5
while tmp<=b :
    if(tmp>=a) :
        print(tmp)
    tmp+=5
    