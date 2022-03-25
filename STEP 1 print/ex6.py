from lib2to3.pgen2.token import RPAR


print(14950)  # 14590  가능
"""
print(abc)    오류!  

""" 
print("abc")
print('abc')            #

print(13 - 2)           #가능
print(12 + 4 / 2 + 1)   #가능
print("A" + "B" + " C") #가능
#print("A" - "B")    # 불가능
print("A" + 'B')   #가능
#print(52-"33")      #불가능