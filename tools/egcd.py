from tools.euclideanDivision import euclideanDivision
from tools.multiply import multiply
from tools.add import add

#compute the inverse (a^-1mod(b))
def egcd (a,b):
    x,y,z,w = [1],[0],[0],[1]
    while b.count(0)!=len(b):       
        q,r = euclideanDivision(a,b)
        a,b =  b,r
        #in GF(2^n) addition and substraction are the same 
        x,y,z,w = z,w,add(x,multiply(q,z)),add(y,multiply(q,w))      
    return x