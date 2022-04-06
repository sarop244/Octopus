a= int(input("입력 :"))

PrimeNumber=[]  #소수 저장하기위한 list
bre=0
for i in range(2,100) :
    count=0
    if i%2==0:      #짝수제외
        continue
    for j in range(1,i+1):
        if i%j==0 :
            count+=1
        if count==2:
            # if PrimeNumber in i:
            #     continue
            # else :
                PrimeNumber.append(i)   #소수 리스트에 넣기
for i in range(len(PrimeNumber)):
    for j in range(i+1):
        if PrimeNumber[i]*PrimeNumber[j]==a:
            bre =PrimeNumber[i]*PrimeNumber[j]
            if i<j :        #큰값 i 에 위치하기
                tmp=i
                i=j
                j=tmp

            print(a,' = ',PrimeNumber[i],' X ',PrimeNumber[j])   
if bre==0:
    print("wrong number")
    
        
