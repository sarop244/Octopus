height = {'jun' :178 , 'Mina' : 164}
print(height.get('jun'))
height['Tom'] =182
print(height)

a= height.pop('Mina')
print(a, height)
height['Robin'] =146
b= height.popitem()
print(b, height)

newheight= {'Billy': 188 , 'Dony' : 172}
height.update(newheight)
print(height)

print(height.keys())
print(height.values())
print(height.items())