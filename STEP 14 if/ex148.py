a= int(input("몇년도인가요? : "))

if((a%4==0 and a%100!=0) or a%400==0)  :
    print("윤년")
else :
    print("평년")