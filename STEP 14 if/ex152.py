colors= ['red', 'orange', 'blue', 'green', 'white', 'black','dark blue', 'purple']

search = input('Enter the color : ')

if(search in colors) :
    print('sorry')
else :
    colors.append(search)
    print(colors[ : ])