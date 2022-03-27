def dikdortgen_cevre_hesapla(a,b):
    return (a+b)*2

def dikdortgen_alan_hesapla(a,b):
    return a*b

a = int(input("Uzun kenar giriniz :"))
b = int(input("Kısa kenar giriniz :"))

print("Dikdörtgenin Çevresi :",dikdortgen_cevre_hesapla(a,b))
print("Dikdörtgenin Alanı :",dikdortgen_alan_hesapla(a,b))