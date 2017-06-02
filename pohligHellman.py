# -*- coding: utf-8 -*-
import argparse
from tools.egcd import egcd
from tools.splitInPrimeFactors import splitInPrimeFactor
from babyStepGiantStep import babyGiantStep
from tools.power import power
import math

#solve the DLP using the pohlig hellman algorithm in GF(2^n)
def pohligHellman(g,p,h,N):
    primes = splitInPrimeFactor(N) #split the given N in primes' power 
                                # for example N=20 primes=[(2, 2), (5, 1)]
    ph = 0
    dlpHasSolution=False
    #for each element in primes, use the baby step/giant step algorithm to solve the DLP
    #and compute the general solution using the chineese remainder algorithm
    for element in primes : 
        primePow = pow(element[0],element[1])
        n = math.ceil(math.sqrt(primePow-1))
        gi = power(g,N//primePow) #compute the power of the given polynomial g
                                #for example g=x ==> gi=x^(N//primePow)
        hi = power(h,N//primePow)
        m = N//primePow
        y = egcd([m],[primePow])[0]
        x =(babyGiantStep(gi,p,hi,n))#x is the solution of the discret logarithm problem in GF(primePow)
        if x == None :
            pass 
        else :
            ph = ph+m*x*y #ph is the solution of discrete logarithm problem in GF(N+1)
            dlpHasSolution = True
    if dlpHasSolution == False :
        return None
    else :
        return ph%N 

def main():
    #==================parse script arguments==================================="
    parser = argparse.ArgumentParser(description="resolve discret logarithm problem (g^x=h), find x", 
                                     usage="this program need 4 arguments : g, p, h and N")
    parser.add_argument('--g', metavar='g', nargs='+', type=int, required =True,
                        help='the generator of the group')
    parser.add_argument("--h", metavar="h", nargs='+', type=int, required=True,
                        help="known function")
    parser.add_argument("--p", metavar="p", nargs='+', type=int, required=True,
                        help="irreducible polynomial, all multiplications in the group G are mod(p)")
    parser.add_argument("--N", metavar="N", nargs='+', type=int, required=True,
                        help="for example in GF(2^15) N=2 15")
    args = parser.parse_args()
    h=args.h
    g=args.g
    p=args.p
    gf=args.N
    N=pow(gf[0],gf[1])
    print(pohligHellman(g,p,h,N))
    
if __name__ == "__main__":
    main()    
#2^9
#--g 0 1 --p 1 0 0 0 1 0 0 1 1 1 --h 0 1 0 0 1 1 1 0 0 --N 2 9
#2^15
#--g 0 1 --p 1 0 0 0 1 0 0 0 1 0 1 0 0 0 0 1 --h 0 1 0 0 1 1 1 0 0 1 0 1 0 1 1 --N 2 15
#2^60
#--g 0 1 --p 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 --h 0 1 1 1 1 0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 1 1 1 0 0 1 1 1 0 1 1 0 1 1 0 1 0 1 0 0 1 0 1 1 0 --N 2 60