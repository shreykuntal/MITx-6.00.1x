print("ATTENTION: CHOOSE NUMBERS ABOVE 1!")
a=int(input("Enter an integer: "))
pwr=1
root=1
b=0
while True:
    
    if root**pwr!=a:
        pwr+=1
        if pwr==6:
            pwr-=5
            root+=1
        if root**pwr==a:
            print(str(root)+'^'+str(pwr)+'='+str(a))
            b+=1
            root+=1
        
        if root**2<=a:
            continue
        if root**2>a:
            break
    if root**1==a:
        print(str(root)+'^'+str(1)+'='+str(a))
            
    
       
    
    
if b<1:
    print("No combinations available")
        
else: 
    print("No more combinations available")
        



             
