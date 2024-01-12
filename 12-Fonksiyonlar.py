def merhabaYaz():
    print("Merhaba")

merhabaYaz()

def ekranaYaz(cumle):
    print("Merhaba " + cumle)


ekranaYaz("Ahmet")

def karesiAL(sayi):
    return sayi ** 2
print(karesiAL(123))

#print(karesiAL("yusuf"))
#karesiAL

def defaultParametreAlanFonksiyon(isim = "Yusuf"):
    print(f"Merhaba {isim}")

defaultParametreAlanFonksiyon()
defaultParametreAlanFonksiyon("Ali")

def birden_cok_sayi_topla(*sayilar):
    toplam = 0
    for s in sayilar:
        toplam+= s
        print(toplam)
birden_cok_sayi_topla(10, 20, 30, 40)

