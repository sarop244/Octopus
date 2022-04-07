list= [[0]*4 for i in range(4)]  #미리 0으로 배열만 지정

for i in range(16):
    list[i//4][i%4] = i            #배열값 지정

for i in range(4):
    print(list[i])