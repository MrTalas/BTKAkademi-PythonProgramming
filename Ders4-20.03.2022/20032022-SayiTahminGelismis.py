import random


while True:
    seviye=input("Bir seviye seç (kolay/orta/zor)").lower() # Girilen kelimeyi küçük harfe çevirir. # .upper() büyük harfe çevirir.

    if seviye=='kolay':
        generate=random.randint(1,10)  #1 ile 10 arasıda rastgele tamsayı üretir
        break
    elif seviye=='orta':
        generate=random.randint(1,50) #1 ile 50 arasıda sayı üretir
        break
    elif seviye=='zor':
        generate=random.randint(1,100)  #1 ile 100 arasıda rastgele tamsayı üretir
        break
    else:
        print("Lütfen (kolay/orta/zor) seçeeklerinden birisini giriniz")




while True:
    tahmin = int(input("Sayıyı Tahmin ediniz :"))
    if tahmin==generate:
        print("Tebrikler doğru bir sayı girdiniz !")
        break
    elif tahmin<generate:
        print("Tahmini büyüt")

    elif tahmin>generate:
        print("Tahmini küçült")