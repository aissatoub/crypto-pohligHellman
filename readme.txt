This programm solves the discret logarithm problem in GF(2^n), all multiplications are modulo p. It finds x for given g, h, and p such that g^x=h. g, p, and h are irreducible polynomials.
The polynomials g, p and h are given as a list of integers from the lowest to the highest degree. For example x^2+x ==> [0,1,1]

For example in GF(2^15),to run this programm in a terminal go to the file crypto and use this command :
py pohligHellman.py --g 0 1 --p 1 0 0 0 1 0 0 0 1 0 1 0 0 0 0 1 --h 0 1 0 0 1 1 1 0 0 1 0 1 0 1 1 --N 2 15
