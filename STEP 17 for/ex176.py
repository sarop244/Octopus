a= int(input('Enter the 1st number : '))
b= int(input('Enter the 1st number : '))

if a>b :
    tmp=a
    a=b
    b=tmp

sum = 0
for i in range(a,b) :
    if i%3==0:
        sum+=i
print('a부터 b 까지 3의 배수의 합은', sum)