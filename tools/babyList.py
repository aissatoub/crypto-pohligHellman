from tools.euclideanDivision import euclideanDivision
from tools.power import power
import math
from tools.multiply import multiply

#return the list of babies' step as a dictionnary
def babiesList(p,g,n):
    babyList = dict()
    babyList[0]=[1]
    gpowi=[1]
    for i in range (1,n):
        gpowi=multiply(g,gpowi)
        generatorPower=euclideanDivision(gpowi,p)
        babyList.update({i:generatorPower[1]})
        #print(babyList)
    return babyList

#N=pow(2,9)-1

#n=math.ceil(math.sqrt(N)) 

#print(babiesList([0,1],[1,0,0,0,1,0,0,1,1,1],n))