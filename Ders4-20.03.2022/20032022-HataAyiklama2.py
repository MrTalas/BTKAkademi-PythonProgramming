try:
    sayi1 =int(input("Bir sayı giriniz"))
    sayi2 = int(input("Bir sayı giriniz"))
    print("Sayıların bölümü",sayi1/sayi2)

except ValueError: # Eğer ValueError hatası verirse alttaki hata mesajını ver.
    print("Girdiğiniz değer int olmalı !")

except ZeroDivisionError:
    print("Bir sayı 0'a bölünemez !")
