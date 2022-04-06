cnt=0
for i in range(24):
    a=i//10
    b=i%10
    for j in range(60):
        c=j//10
        d=j%10
        if a==3 or b==3 or c==3 or d==3:
            cnt+=1
print(cnt)