def isIn(a,b):
    for i in range(len(b)):
        if b[i] in a:
            return True
    return False
isIn('abcd','ghjk')