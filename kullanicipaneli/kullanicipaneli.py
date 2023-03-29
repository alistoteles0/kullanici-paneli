print("Kayıt ol")
syskullanici_adi=input("Kullanıcı adı: ")
syssifre=input("Şifre: ")
print("Giriş")
while True:
    kullanici_adi=input("Kullanıcı adı: ")
    sifre=input("Şifre: ")
    if (kullanici_adi != syskullanici_adi and sifre == syssifre):
        print("Girdiğiniz kullanıcı adında bir hesap yoktur. Lütfen tekrar deneyiniz.")
    elif (kullanici_adi == syskullanici_adi and sifre != syssifre):
        print("Girdiğiniz şifre yanlıştır. Lütfen tekrar deneyiniz.")
    elif (kullanici_adi != syskullanici_adi and sifre != syssifre):
        print("Kullanıcı adı ve şifre yanlış. Lütfen tekrar deneyiniz.")
    else:
        print("Giriş yapıldı.")
        break
    
        