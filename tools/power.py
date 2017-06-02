from tools.multiply import multiply

#compute the polynomial a to the power of n , using the exponentiation by squaring algorithm    
def power(a, n):
    b, m = a, n
    r = [1]*len(b)
    i=0
    while m > 0:
        if m % 2 == 1:
            if i==0 :
                r=b
                i=5
            else :
                r = multiply(r, b)
        b = multiply(b, b)
        m = m //2
    return r 