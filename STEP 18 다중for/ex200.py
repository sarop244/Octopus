a= [1,2,3,4,5]
list=[]
for i in a:
    for j in a:
        for k in a:
            for l in a:
                for m in a:
                    tmp= str(i) + str(j) +str(k) +str(m) + str(l)
                    if len({i,j,k,l,m})==5:
                        list.append(int(tmp))
list.sort()
print(list[49])