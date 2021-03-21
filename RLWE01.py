"""
Homomorphic Encryption
Example for ring-learning-with-errors
Based on Fan, Junfeng, and Frederik Vercauteren. ‘Somewhat Practical Fully Homomorphic Encryption’, 2012. https://eprint.iacr.org/2012/144 .
"""

import numpy as np
from numpy.polynomial import Polynomial as poly

"""
Declaration of addition and multiplication of two polynomials x_1 and x_2 modulo the polynomial modP
on the residual class ring Z/modS*Z
"""

def polyaddMod(x_1, x_2, modS, modP):
    return poly(((x_1 + x_2).coef % modS)) % modP


def polymulMod(x_1, x_2, modS, modP):
    return poly((poly((x_1 * x_2).coef % modS) % modP).coef % modS)
    
"""
Generators of polynomes with random coefficients needed for the key generator
"""

def rnd_binary_coef(length):
    return poly(np.random.randint(0, 2, length))

def rnd_uniform_coef(length, modS):
    return poly(np.random.randint(0, modS, length))

def rnd_normal_coef(length):
    return poly(np.random.normal(0, 2, length))

"""
The key generator returning the public and secret key
"""
def keyGenerator(length, modS, modP):
    sk = rnd_binary_coef(length) #secret key
    a  = rnd_uniform_coef(length, modS) #first part of the public key
    e  = rnd_normal_coef(length) #noise
    b  = - polyaddMod(polymulMod(a, sk, ms, mp), e, ms, mp) #second part of the public key
    return (a,b), sk #public and secret key
    
"""
Encryption function, adding noise e1 and e2
"""

def enCrypt(pt, pk, q, t, modP):
    l = pk[0].coef.size #key length
    m = poly(pt % t)
    d = int(q / t) #delta to regulate the 
    e1 = rnd_normal_coef(l)
    e2 = rnd_normal_coef(l)
    u = rnd_binary_coef(l)
    
    ct0 = polyaddMod(polyaddMod(polymulMod(pk[0], u, q, mp), e1, q, modP), d * m, q, modP)
    ct1 = polyaddMod(polymulMod(pk[1], u, q, mp), e2, q, modP)
    
    return (ct0, ct1) #the cypher text consists of two polynomials
    
"""
Decryption function, retrieving the plain text by applying the secret key as the base of the vector space to filtre out the noise terms
"""
def deCrypt(ct, sk, q, t, modP):
    dpt = polyaddMod(polymulMod(ct[1], sk, q, mp), ct[0], q, modP)
    
    dt = (dpt.coef * t/q) % t
    return round(dt[0],0)
    
"""
Let's try it out
"""
ms = 11  #the modulus defining the integer residual class Z/{ms}
mp = poly([1,0,0,0,1]) #the modulus defining the polynomial residual class Z(ms)/{mp}

k = keyGenerator(20,ms,mp) #generating the key

pk = k[0] #public key
sk = k[1] #secret key

q = 7919 #q and t defining the noise via the delta d
t = 17

pt1 = 2 #plain text 1
pt2 = 4 #plain text 2

ct1 = enCrypt(pt1, pk, q, t, mp) #cypher text of plain text 1 using only the public key
ct2 = enCrypt(pt2, pk, q, t, mp) #cypher text of plain text 2

ct = np.polyadd(ct1,ct2) #adding the two cypher texts

decrypted = deCrypt(ct, sk, q, t, mp) #decrypting the sum using the secret key
decrypted
