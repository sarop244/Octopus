list = [5,1,7,2,6,3]
def swap(i,j) :
    tmp=list[i]
    list[i]=list[j]
    list[j]=tmp
i, j = 3, 5
swap(i,j)
print(list)