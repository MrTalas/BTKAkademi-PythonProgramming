#Kendisine gönderilen kullanıcı adı ve şifreye göre kontrol yapan ve True ya da False olarak değer gönderen bir fonksyion yazınız.
#Kullanıcı adı = admin , Şifre = 123456 Olursa True,Bilgiler yanlış girilirse False


def check(username,password):
    if username == 'admin' and password == '123456':
        kontrol = True
    else:
        kontrol = False
    return kontrol

kullanici_adi = input("Kullanıcı adı giriniz :")
parola = input("Parola adı giriniz :")
kontrol = check(kullanici_adi,parola)
if kontrol == True:
    print("Giriş başarılı")
else:
    print("Giriş yapılamadı")