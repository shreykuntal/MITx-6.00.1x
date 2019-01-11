def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    
    idea : bisection search and recursion
    '''
    if char == aStr[len(aStr)//2]:
        return True
    elif len(aStr) < 2:
        return False
    else:
        if char > aStr[len(aStr)//2]:
            aStr = aStr[len(aStr)//2:len(aStr)]
        else:
            aStr = aStr[0:len(aStr)//2]
        return isIn(char, aStr)