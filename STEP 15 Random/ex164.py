import random

cars = ['Hyundai', 'Kia', 'BMW', 'Benz']

print("original : ", cars)

random.shuffle(cars)

print("change : ", cars)

if cars[0]=='Hyundai' :
    print("True")
else :
    print("False")