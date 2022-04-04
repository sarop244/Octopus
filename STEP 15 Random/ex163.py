import random

level1 = random.randint(1,2)
level2 = random.randint(1,4)
level3 = random.randint(1,8)

a= int(input("level1 (1~2) : "))
if a==level1 :
    print("Correct!")
else :
    print("Failure!")
    print("Answer is :" , level1)

b= int(input("level1 (1~4) : "))
if b==level2 :
    print("Correct!")
else :
    print("Failure!")
    print("Answer is :" , level2)

c= int(input("level1 (1~8) : "))
if c==level3 :
    print("Lucky!!!!!")
else :
    print("Failure!")
    print("Answer is :" , level3)