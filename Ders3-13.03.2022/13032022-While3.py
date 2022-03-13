while True:
    username=input("Kullanıcı adı:")
    password=input("Parola:")
    if username=='admin' and password=='123456':
        break
    else:
        print("Hatalı kullanıcı adı veya parola")
print("Sisteme başarılı olarak giriş yaptınız")