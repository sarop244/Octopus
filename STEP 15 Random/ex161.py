import random

a= int(input('두 정수를 입력하시오 : '))
b= int(input())

if(a==b or abs(a-b)==1) :
    print("no integer between two numbers")
else :
    print(random.randrange(min(a,b)+1,max(a,b)))
