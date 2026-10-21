from math import gcd
from sympy import randprime, integer_nthroot, factorint
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

    # funkcija grazina tikslią e-tojo laipsnio sveika saknies dali iš c
    m, tiksli_saknis = integer_nthroot(c, e)
    if not tiksli_saknis:
        raise ValueError("c nera tikslus e-tojo laipsnio skaicius.")

    tekstas = int_to_string(m)
    return m, tekstas


def RSA_mazo_daliklio_ataka(c, e, n):
    
    # isskaido n i pirminius daliklius
    dalikliai = factorint(n)
    phi = 1
    for p, laipsnis in dalikliai.items():
        phi *= p ** (laipsnis - 1) * (p - 1)

    d = pow(e, -1, phi)
    m = pow(c, d, n)

    tekstas = int_to_string(m)
    return m, tekstas


def RSAES_PKCS1_v1_5_atifravimas(c, d, n):

    k = byte_length(n)
    m = pow(c, d, n).to_bytes(k, "big")

    if m.startswith(b"\x00\x02"):
        ps_start = 2
    # priima nestandartini bloka be pradinio 00 baito
    elif m.startswith(b"\x02"):
        ps_start = 1
    else:
        raise ValueError("Isšifruotas blokas neturi PKCS#1 v1.5 0x02 prefikso.")

    separator = m.find(b"\x00", ps_start)
    # patikrina, ar užpildas yra bent 8 baitu, būtina PKCS1 v1.5 formato patikrai
    if separator < ps_start + 8:
        raise ValueError("PKCS#1 v1.5 užpildas yra netinkamas arba per trumpas.")

    tekstas = bytes_to_string(m[separator + 1:])
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
    m4, tekstas4 = RSA_mazo_daliklio_ataka(c4, e4, n4)
    
    print("\n4. \nAtkurtas m4 =", m4)
    print("Atkurtas tekstas:", tekstas4)


    # 5.uzd
    d5 = 68915707967092233714016724205907872801815457202766306899046387439954479168083
    n5 = 103373561950638350571025086308861809203366935441586383691348419905014873924061
    c5 = 47325451040894553143035341811924169794297859883472909852692863847232714906497
    m5, tekstas5 = RSAES_PKCS1_v1_5_atifravimas(c5, d5, n5)
    print("\n5. \nAtkurtas m5 =", m5)
    print("Atkurtas tekstas:", tekstas5)
    

 
 
