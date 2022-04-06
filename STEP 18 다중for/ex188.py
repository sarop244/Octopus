a=input("입력 :") 

for i in range(0,len(a)) :
    for j in range(0,i+1) :
        print(a[j],end='')
    print( )  