import random

ran4 = []
for i in range(4) :
    a= random.randint(10,20)
    ran4.append(a)
print("4가지 수 : " ,ran4)

avg = sum(ran4)

print("평균 : " , avg/4)

if avg/4>=15 :
    print("Big") 
else :
    print("Small")