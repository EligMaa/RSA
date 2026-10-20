# RSA

Užduotis:

1. Sugeneruoti RSA kriptosistemos viešąjį ir privatųjį raktą, kai duotas e, o p ir q 256 bitų ilgio.
2. Užšifruokite savo vardą ir pavardę 1 užduotyje gautu viešuoju raktu.
3. Nulaužkite slaptaraštį c užšifruotą viešuoju raktu (e, n), kai žinoma, kad me < n. Duotas viešasis raktas.
4. Nulaužkite slaptaraštį c užšifruotą viešuoju raktu (e, n), kai žinoma, kad vienas iš n daliklių yra mažas (40 bitų). Duotas viešasis raktas.
5. Atšifruokite slaptaraštį c prailgintą RSAES-PKCS1-v1_5 schema užšifruotą viešuoju raktu (e, n).  Duotas privatusis raktas.

Tekstai koduojami UTF-8 koduote.
Pagalbinės funkcijos, skirtos konvertuoti tekstą į skaičių, faile pagalbines_funkcijos.py.
Užduočių variantai faile variantai.zip. Spręsti užduotį esančią faile variantas.txt.

Užduoties failo struktūra:
1.
e
 3.
(e, n)
c
4.
(e, n)
c
5.
(d, n)
c

