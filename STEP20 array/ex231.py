alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alph = list(alph)
a= list(input(" 입력 :").upper())

for i in alph :
    if not (i in a):
        print(i,end="")