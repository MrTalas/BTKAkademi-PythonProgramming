"""
Kullanıcı yıl sonu ortalamasını girsin,ortalama 85 üstüyse taktir belgesi,70 üstü ise teşekkür belgesi,bunların dışında ise hiçbir belge alamasın.


"""

sayi = int(input("Ortalama giriniz : "))

if sayi >= 85:
    print("Taktir belgesi almaya hak kazandınız.")
if sayi>= 70 and sayi < 85:
    print("Teşekkür belgesi almaya hak kazandınız.")
if sayi < 70:
    print("Hiçbir belge alamıyorsunuz.")

