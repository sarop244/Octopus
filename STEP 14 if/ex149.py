#두수의 차
a= int(input('a='))
b= int(input('b='))

if a<b :
    print(b-a)
elif b<a :
    print(a-b)
else :
    print("0")


#세 수의 입력
c= int(input('c='))
d= int(input('d='))
e= int(input('e='))

tmp = [c,d,e]
tmp.sort()

print(tmp[2]*tmp[0]-tmp[1])