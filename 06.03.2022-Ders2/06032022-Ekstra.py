"""
Kullanıcı yıl sonu ortalamasını girsin,ortalama 85 üstüyse taktir,70 üstü ise teşekkür,bunların dışında ise boş geçsin.


"""

sayi = int(input("Ortalama giriniz : "))

if sayi >= 85:
    print("Taktir alıyorsun")
if sayi>= 70 and sayi < 85:
    print("Teşekkür alıyorsun")
if sayi < 70:
    print("Boş")

