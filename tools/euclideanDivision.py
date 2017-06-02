from tools.shiftList import shiftListToTheRight
'''
Created on 20 mars 2017

@author: barry
'''

#delete zeros on the right
#examples : normalize([0,0,0,1]) gives [0, 0, 0, 1]
#normalize([1,0,0,0,0]) gives [1]
#normalize([0,0,0,0,0]) gives [0]
def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)
    return poly

def polyDivmod(num, den):
    #Create normalized copies of the args
    num = num[:]
    normalize(num)
    den = den[:] #a[:] = [0, 0, 0] replace elements in the original list
    normalize(den)
    if len(num) >= len(den):
        #Shift den towards right so it's the same degree as num
        shiftlen = len(num) - len(den)
        #den = [0] * shiftlen + den
        den = shiftListToTheRight(den,shiftlen)
    else:
        for i in range(len(num)):
            num[i] = num[i]%2
        return [0], num
    quot = [0]
    divisor = (den[-1])
    if len(num) == 1 and len(den) == 1:
        quot[0] = (num[0]//den[0])%2
        num[0] = (num[0]%den[0])%2
        return quot,num
    for i in range(shiftlen + 1):
        #Get the next coefficient of the quotient.
        mult = (num[-1] // divisor)%2
        quot = [mult] + quot        
        #Subtract mult * den from num, but don't bother if mult == 0
        #Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in den]
            num = [(u - v)%2 for u, v in zip(num, d)]
        num.pop()
        den.pop(0)
    normalize(num)
    return quot, num
#[a0...an]
def euclideanDivision(num, den):
    q, r = polyDivmod(num, den)
    return q, r





