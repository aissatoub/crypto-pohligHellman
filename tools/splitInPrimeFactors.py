import math
#===============function which split given number in the power of prime numbers========
def splitInPrimeFactor(k):
    primeFactors = []  # prime factors of n (duplication possible)
    divider = 2  # prime divider of n
    while divider <= math.sqrt(k):  # when the divider  reach the sqrt of n it means we can't find a factor 
        if k % divider == 0:
            primeFactors += [divider]
            k //= divider
        else:
            divider += 1
    primeFactors += [k]
    #return a tuple of the primes, each element of the tuple is a set a 2 elements 
    #the first element is the prime and the second one is the number of times it's duplicate in the list primeFactors
    #example primeFactors=[2,2,3,2,5,3] the result will be [(2,3),(3,2),(5,1)]
    return sorted([(divider, primeFactors.count(divider)) for divider in set(primeFactors)], key=lambda x: x[0])
