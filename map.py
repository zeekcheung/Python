def normalize(x):
    r = ''
    if(isinstance(x,str)):       
        r = r + x[0].upper()
        for s in x[1:]:
            r = r + s.lower()
    else:
        r = r + 'NotStr'
    return r
    
L1 = ['adam', 'LISA', 'barT']
L2 = map(normalize,L1)                # map(funcname,list)
print(next(L2))                       # return an iterator
#print(list(L2))                      


