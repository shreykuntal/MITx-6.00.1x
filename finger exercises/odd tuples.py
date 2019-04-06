def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    toPrint = ()
    for i in range(0, len(aTup), 2):
        toPrint += (aTup[i],)
    return toPrint
print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))