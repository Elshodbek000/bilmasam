lugat = {
    "ism": "Ali",
    "yosh": 18
}

lugat["universitet"] = "TATU"

print(lugat.keys())
print(lugat.values())
mahsulotlar = {
    "olma": 10000,
    "banan": 20000,
    "anor": 15000
}

nom = input("Mahsulot nomini kiriting: ")

if nom in mahsulotlar:
    print("Narxi:", mahsulotlar[nom], "so'm")
else:
    print("Mahsulot topilmadi")
telefon = {
    "Ali": "901234567",
    "Vali": "911234567"
}

ism = input("Ism kiriting: ")

if ism in telefon:
    print("Telefon raqami:", telefon[ism])
else:
    print("Bu ism topilmadi")

    yangi_ism = input("Yangi ism kiriting: ")
    yangi_raqam = input("Telefon raqamini kiriting: ")

    telefon[yangi_ism] = yangi_raqam

print(telefon)
gap = input("Gap kiriting: ")

sozlar = gap.split()
sanoq = {}

for soz in sozlar:
    if soz in sanoq:
        sanoq[soz] += 1
    else:
        sanoq[soz] = 1
print(sanoq)