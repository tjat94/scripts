from sympy import factorint
from Crypto.Util.number import inverse, long_to_bytes

# Given values
n = 43941819371451617899582143885098799360907134939870946637129466519309346255747
e = 65537
c = 9002431156311360251224219512084136121048022631163334079215596223698721862766

# Factor n
factors = factorint(n)
p, q = factors.keys()
#205237461320000835821812139013267110933, 214102333408513040694153189550512987959
print("Prime factors:")
print("p =", p)
print("q =", q)

phi_n = (p - 1) * (q - 1)
print("Phi(n) =", phi_n)

d = inverse(e, phi_n)
print("Private key (d):", d)

plaintext = pow(c, d, n)
flag = long_to_bytes(plaintext)
print(flag.decode())
print("Decrypted Plaintext:", flag)