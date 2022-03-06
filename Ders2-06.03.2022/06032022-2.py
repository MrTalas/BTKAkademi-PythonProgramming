#Kullanıcıdan isim soyisim telefon numarası alarak bir listeye aktarınız.


bilgiler = []


name = input("İsminiz ? ")
surname = input("Soyisminiz ? ")
phonenumber = input("Telefon numaranız ? ")

bilgiler.append(name)
bilgiler.append(surname)
bilgiler.append(phonenumber)

print("İsim",bilgiler[0])
print("Soyisim",bilgiler[1])
print("Telefon Numarası",bilgiler[2])