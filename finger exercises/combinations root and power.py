while True:
    a=int(input("Enter an integer: "))
    pwr=1
    root=1
    b=0
    c=0
    if a<0:
        a=abs(a)
        c=1
    elif a<0 and a%2==0:
        quit=1
    elif a==-1 or a==-2:
        quit=1
    elif a<3:
        quit==1
    while True:
        if quit==1:
            break 
        if pwr==100:
            pwr-=99
            root+=1
        if (c==1) and (pwr%2!=0) and (root**pwr==a): 
            print('-'+str(root)+'^'+str(pwr)+'='+'-'+str(a))
            b+=1
            root+=1
        elif (root**pwr==a) and (c==0):
            print(str(root)+'^'+str(pwr)+'='+str(a))
            b+=1
            root+=1       
        pwr+=1
        if root**2<=a:
            continue
        if root**2>a:
            break     
    if b<1:
        print("No combinations available")
    else: 
        print("No more combinations available")
    ask=input("(y) for more. (n) to exit: ")
    if ask=='y':
        continue
    elif ask=='n':
        break
    else:
        print("Are you blind folded?! The program is now quitting!")
        break


                
