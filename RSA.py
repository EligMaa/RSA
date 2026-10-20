from math import gcd
from sympy import randprime, integer_nthroot
from pagalbines_funkcijos import *


def pirminiu_sk_generavimas():
    # generuojami pirminiai skaiciai p ir q, kurie yra 256 bitu ilgio
    while True:
        p = randprime(2**255, 2**256)
        q = randprime(2**255, 2**256)
        phi = (p - 1) * (q - 1)

        if p != q and gcd(e, phi) == 1:
            break

    return p, q

def viesasis_raktas(p, q):
    N = p * q
    phi = (p - 1) * (q - 1)
    return N, phi

def privatus_raktas(phi):

    d = pow(e, -1, phi)
    return d


def RDA_sifravimas(vardas, e, N):
    int_vardas = string_to_int(vardas)

    sifras = pow(int_vardas, e, N)
    return sifras


def RSA_mazo_laipsnio_ataka(c, e, n):
    if c >= n:
        raise ValueError("Salyga m**e < n netenkinama: c turi buti mazesnis uz n.")

    # funkcija grazina tikslią e-tojo laipsnio sveika šaknies dali iš c
    m, tiksli_saknis = integer_nthroot(c, e)
    if not tiksli_saknis:
        raise ValueError("c nera tikslus e-tojo laipsnio skaicius.")

    tekstas = int_to_string(m)
    return m, tekstas






if __name__ == "__main__":

    # 1.uzd
    e = 63079
    p, q = pirminiu_sk_generavimas()
    N, phi = viesasis_raktas(p, q)
    print(f"\n1.\nViesasis raktas: ({e}, {N})")

    d = privatus_raktas(phi)
    print(f"Privatus raktas: ({d}, {N})")
    print("p =", p)
    print("q =", q)

    # 2.uzd
    sifras = RDA_sifravimas("Rugile Macaite", e, N)
    print("\n2.\nUzsifruotas tekstas: Rugile Macaite - ", sifras)


    # 3.uzd
    c3 = 426463887070522428375487415625613894747681
    e3 = 3
    n3 = 37386062049434900256037443508623318748753814612569840277854120419508766843023
    m, tekstas = RSA_mazo_laipsnio_ataka(c3, e3, n3)
    print("\n3. \nAtkurtas m =", m)
    print("Atkurtas tekstas:", tekstas)


    # 4.uzd
    c4 = 17887767281603474295427299910264582824834805686489458772922224970590317665457
    e4 = 65537
    n4 = 50198363198492354510796846792248778849154207577262255195939215967243214950367
    





