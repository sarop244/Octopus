
sum=0
i=1
while True :
    if i%2==1 :
        sum+=i
    if i%2==0 :
        sum+=-(i)

    if sum>=100 :
        break

    i+=1
print(i)