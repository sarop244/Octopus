a= input('Enter : ')
b= a.split()

if(b[1]=='+') :
    print(int(b[0]) + int(b[2]))
elif b[1]=='-' :
    print(int(b[0]) - int(b[2]))
elif b[1]=='*' :
    print(int(b[0]) * int(b[2]))
elif b[1]=='/' :
    print(int(b[0]) / int(b[2]))