from tools.power import power
import math
#=================================
def egcd (a,b):
    x,y,z,w = 1,0,0,1
    while b != 0:
        q,r = divmod(a,b)
        a,b =  b,r
        x,y,z,w = z,w,x-q*z,y-q*w
        #print(x,y,z,w,a,b)
    return a,x,y

#=============solve the DLP with babysteps/giantSteps algo=============================
def babiesList(p,g):
    babySteps = dict()
    for i in range (p):
        babySteps.update({i:pow(g,i)%p})
    return babySteps

def babyGiantStep(g,p,h):
    babyDict = babiesList(p,g)
    giantSteps = dict()
    hmod = h%p
    #inv1 = (egcd(g,p)[1])%p
    inv2 = (egcd(pow(g,p),p)[1])%p
    print("****egcd*******")
    print(egcd(pow(g,p),p))
    print("***********")
    for j in range(p):
        giant = (hmod*(pow(inv2,j)))%p
        giantSteps.update({j:giant}) 
        if giant in babyDict.values():
            babyKey = [c for c,v in babyDict.items() if v==giant]
            return babyKey[0]+j*p, giantSteps #return the solution of the DLP and the giant steps
            
#===============fonction which split given number in the power of prime numbers========
def splitInPrimeFactor(k):
    primeFactors = []  # prime foctors of p (duplication possible)
    divider = 2  # prime divider of p
    while divider <= math.sqrt(k):  # when the divider  reach the sqrt of p it means we can't find a factor 
        if k % divider == 0:
            primeFactors += [divider]
            k //= divider
        else:
            divider += 1
    primeFactors += [k]
    return sorted([(divider, primeFactors.count(divider)) for divider in set(primeFactors)], key=lambda x: x[0])

#==============chinese reminder==================
def chineseReminder(g,p,h):
    primes=splitInPrimeFactor(p)
    ph=0
    for element in primes :
        primePow = pow(element[0],element[1])
        gi = (pow(g,p//primePow))%p
        hi = (pow(h,p//primePow))%p
        m=p//primePow
        y=(egcd(m,primePow)[1])%primePow
        x=babyGiantStep(gi,primePow,hi)
        ph=ph+m*x*y
    return ph%p   
print(chineseReminder(3,113,57))
     









