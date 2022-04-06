for i in range(1,12):
    if i <= 5:
        print(" "*(6-i), end="")
        print("*"*(2*i-1))
    else :
        print(" "*(i-6), end="")
        print("*"*(2*(11-i)+1))