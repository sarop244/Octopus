
count=0
a= int(input("입력 : "))

for i in range(1,a+1) :
    if i%10==1 :
        count+=1
    if i//10==1:
        count+=1

print(count)