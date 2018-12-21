s='12321.12341,12441.245541,25563.4932,56477.3452'#your numbers here
a=s.split(',')
total=0
for i in a:
    total=total+float(i)
print(total)
