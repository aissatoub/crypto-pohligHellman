This programm solves the discret logarithm problem in GF(2^n), all multiplications are modulo p. It finds x for given g, h, and p such that g^x=h. g, p, and h are irreducible polynomials.
The polynomials g, p and h are given as a list of integers from the lowest to the highest degree. For example x^2+x ==> [0,1,1]

g, p and should be irreducible.

For example in GF(2^15),to run this programm in a terminal go to the file crypto-pohligHellman and use this command :
py pohligHellman.py --g 0 1 --p "coef of poly p" --h "coef of poly h" --N 2 15
