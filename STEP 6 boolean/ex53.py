from xmlrpc.client import boolean


boolean_1 = False
boolean_2 = ~True
#boolean_3 != True
boolean_4 = True == True
boolean_5 = True == False
boolean_6 = True > True
boolean_7 = True > False
boolean_8 = False > True

print(boolean_1)  #False
print(boolean_2)  #-2   ????
#print(boolean_3)   이건 error
print(~boolean_4)  # True
print(~boolean_5)  # -1
print(~boolean_6)  # -1
print(~boolean_7)  # -2
print(~boolean_8)  # -1