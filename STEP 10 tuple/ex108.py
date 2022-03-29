myTuple = ('a','b',(1,2,3),[4,5,6])
print(myTuple)
print(myTuple[1])

print(myTuple[2][0])
print(myTuple[3][2])

#myTuple[2][0] = 0  () 는 튜플이므로 못바꿈
myTuple[3][0] = 0
print(myTuple)    #[] 는 리스트이므로 가능
