for_odds =[1,2,3,4,5,6,12344221,9,9,10] #your list here #random.sample(range(150), 100) # 100 random numbers b/w 0,150
biggest_odd=float('-inf')

for i in for_odds:
	if i%2!=0:
		if i>biggest_odd:
			biggest_odd=i

print("The greatest odd number is ", biggest_odd)
"""
while j>=biggest_odd:
        j-=1
        if j%2!=1 and j==for_odds[:]:
                print("The second largest odd is ", j)"""



j=len(for_odds)
f=(len(for_odds)-1)
while True:
        if j<biggest_odd and j%2!=0 and j==for_odds[f]:
                print("The second largest odd number is ",j)
                break
        j-=1
        f-=1
                
        
        
                
        



   
    


    
    
        

    
