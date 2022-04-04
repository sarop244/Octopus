a = int(input("입력 : "))

print('음수') if(a<0) else print('양수')
print('홀수') if(a%2==1) else print('짝수')
print('3의 배수 O') if(a%3==0) else print('3의 배수 X')
print('5의 배수 O') if(a%5==0) else print('5의 배수 X')