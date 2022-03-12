print(""" 
[1]Toplama
[2]Çıkarma
[3]Çarpma
[4]Bölme
""")
deger = int(input("İşlem seç: "))

if deger == 1:
    print("Toplama İşlemi")
    a = input("1.sayı : ")
    b = input("2.sayı : ")
    sonuc = int(a)+int(b)
    print(a,"+",b,"=",sonuc)
    
if deger == 2:
    print("Çıkarma İşlemi")
    a = input("1.sayı : ")
    b = input("2.sayı : ")
    sonuc = int(a)-int(b)
    print(a,"-",b,"=",sonuc)    

if deger == 3:
    print("Çarpma İşlemi")
    a = input("1.sayı : ")
    b = input("2.sayı : ")
    sonuc = int(a)*int(b)
    print(a,"x",b,"=",sonuc)    
    
if deger == 4:
    print("Bölme İşlemi")    
    a = input("1.sayı : ")
    b = input("2.sayı : ")
    sonuc = int(a)/int(b)
    print(a,"÷",b,"=",sonuc)    
