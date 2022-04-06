a= int(input("입력 : "))

count=1

while a!=1 :
    if a%2==0 :
        a=a//2

    else :
        a=2*a +2

    count+=1
print(count)