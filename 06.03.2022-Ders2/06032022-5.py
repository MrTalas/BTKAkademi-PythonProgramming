"""
>  Büyüktür
<  Küçüktür
>= Eşiti veya büyüğü mü
<= Eşiti veya küçüğü mü
!  Eşit değildir
== Eşit mi
"""

cinsiyet = input("Harf giriniz :")

if cinsiyet == "e" or cinsiyet == "E":
    print("Cinsiyet olarak Erkek girdiniz")
    print("İf içerisi")
elif cinsiyet == "k" or cinsiyet == "K":
    print("Cinsiyet olarak Kadın girdiniz")
    print("Eİf içerisi")
else:
    print("E ya da K giriniz")
print("Şuanda if dışındasın")