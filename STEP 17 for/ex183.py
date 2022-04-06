a=int(input("입력1 : "))
b=int(input("입력2 : "))


if b<a :
    tmp=a
    a=b
    b=tmp

sum=0

for i in range(a,b+1) :
    if i%2==0 :
        tmp = -(i)
        sum+=tmp
        print(' ',tmp,end='')
    if i%2==1 :
        sum+=i
        print(' +',i,end='')
print('=',sum)