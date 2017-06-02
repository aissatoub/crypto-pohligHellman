def add(p1,p2):
    "Return a new plist corresponding to the sum or the substraction of the two input lists." 
    "[a0,...,an]"
    lenght = max(len(p1),len(p2))
    new = [0]*lenght
    if len(p1) > len(p2):
        p2 = p2+[0]*(len(p1)-len(p2))
    elif len(p2)>len(p1):
        p1 = p1+[0]*(len(p2)-len(p1))
    for i in range(lenght):
        new[i] = (p1[i]+p2[i])%2
    return new