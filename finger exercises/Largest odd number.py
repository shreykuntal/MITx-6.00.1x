def type(x,y,z):
    if x%2!=0 and y%2!=0 and z%2!=0:
        if x>y and x>z:
            print (x,("is largest odd number"))
        elif y>x and y>z:
            print (y,("is largest odd number"))
        elif z>x and z>y:
            print (z,("is largest odd number"))
        else:
            print("All three are same")
    elif x%2!=0 and y%2!=0:
        if x>y:
            print (x,("is largest odd number"))
        elif y>x:
            print (y,("is largest odd number"))
        else:
            print("z is not an odd number. x and y are same")
    elif x%2!=0 and z%2!=0:
        if x>z:
            print (x,("is largest odd number"))
        elif z>x:
            print (z,("is largest odd number"))
        else:
            print("y is not an odd number. x and z are same")
    elif y%2!=0 and z%2!=0:
        if y>z:
            print (y,("is largest odd number"))
        elif z>y:
            print (z,("is largest odd number"))
        else:
            ("x is not an odd number. z and y are same")
    elif x%2!=0:
        print (x,("is the largest odd number"))
    elif y%2!=0:
        print (x,("is the largest odd number"))
    elif z%2!=0:
        print (x,("is the largest odd number"))
    else:
        print("None of them are odd")
    
type(-25,-85,-11)

    
