a= int(input("Enter the number :"))
if a==1 :
    print('소수아님')

for i in range(1,a) :
    if a%i==0 and i!=1:
        print("소수아님")
        break
    if i==a-1 :
        print("소수") 