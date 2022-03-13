tutulansayi=6
sayac=1


while True:
    sor = int(input("Sayıyı tahmin et :"))
    if sayac == 3:
        print("Doğru sayı buydu", tutulansayi)
        break
    if sor == tutulansayi:
        print("Doğrı tahmin ettiniz")
        break
    elif sor > tutulansayi:
        print("Sayıyı küçült")
        sayac+=1
    elif sor < tutulansayi:
        print("Sayıyı büyült")
        sayac+=1
