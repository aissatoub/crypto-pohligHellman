from tools.add import add
from tools.shiftList import shiftListToTheRight

#multiply x and y using the karatsuba algorithm    
def multiply(x,y):
    if min(len(x),len(y)) == 0: 
        return [0]
    m = max(len(x),len(y))
    if (m == 1): 
        return [(x[0]*y[0])%2]
    else: m >>= 1
    x0,x1 = x[:m],x[m:] #split x and y in to parts
    y0,y1 = y[:m],y[m:]
    z0 = multiply(x0,y0)
    z1 = multiply(x1,y1)
    z2 = multiply(add(x0,x1),add(y0,y1))
    t1 = shiftListToTheRight(add(z2,add(z1,z0)),m)
    t2 = shiftListToTheRight(z1,m*2)
    return add(add(z0,t1),t2)