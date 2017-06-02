from tools.euclideanDivision import euclideanDivision
from tools.power import power
from tools.multiply import multiply
from tools.egcd import egcd
from tools.babyList import babiesList

#solve the discret logarithm problem (DLP) in GF(2^n) using the baby step/giant step algorithm
def babyGiantStep(g,p,h,n):
    babyDict = babiesList(p,g,n)
    print("babies' step")
    print(babyDict)
    giantSteps = dict()
    giantSteps[0]=[1]
    hmod = euclideanDivision(h,p)[1]
    egc = egcd(power(g,n),p)
    inv = euclideanDivision(egc,p)
    inpowj=[1]
    for j in range(1,n):
        inpowj=multiply(inv[1],inpowj)
        #a = power(inv[1],j)
        b = multiply(hmod,inpowj)
        giant = euclideanDivision(b,p)
        giantSteps.update({j:giant[1]})
        print("giants' step")
        print(giantSteps)
        if giant[1] in babyDict.values(): #verify if we have a collision
            print("the solution x for g^x=h is :")
            babyKey = [c for c,v in babyDict.items() if v==giant[1]]
            return babyKey[0]+j*n #return the solution of the DLP 