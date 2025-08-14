#!/usr/bin/python3
#credit to jaxafed
# gmpy2 is a C-coded Python extension module that supports
# multiple-precision arithmetic.
# pip install gmpy2
from gmpy2 import isqrt
from Crypto.PublicKey import RSA


def factorize(n):
    # since even nos. are always divisible by 2, one of the factors will
    # always be 2
    if (n & 1) == 0:
        return (n/2, 2)

    # isqrt returns the integer square root of n
    a = isqrt(n)

    # if n is a perfect square the factors will be ( sqrt(n), sqrt(n) )
    if a * a == n:
        return a, a

    while True:
        a = a + 1
        bsq = a * a - n
        b = isqrt(bsq)
        if b * b == bsq:
            break

    return a + b, a - b

pub_key = RSA.importKey(open("id_rsa.pub","rb").read())
print(f"Length of public key in bits {pub_key.size_in_bits()}")
print(f"Last 10 digits of public key: {str(pub_key.n)[-10:]}")
p,q = factorize(pub_key.n)
print(f"Numerical difference between p and q is: {p-q}")
phi = (p-1)*(q-1)
d = pow(pub_key.e,-1,phi)

priv_key = RSA.construct((pub_key.n,pub_key.e,int(d)))
open("id_rsa","wb").write(priv_key.export_key())
