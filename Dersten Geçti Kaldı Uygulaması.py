#Dışarıdan İki Sayı Alınacak ve Geçme Notu ve Alınan Notu Girilecek ve Öğrenci Geçti veya Kaldı Diyecek 
# Notu 90 üzeri ise Çok Başarılısınız Mesajı versin.
gecmenotu=int(input('Geçme Notu Giriniz'))
alinannot=int(input('Aldığın Notu Gir'))
if alinannot>=gecmenotu:
    print('Dersi Geçtiniz')
    if alinannot>=90:
        print('Çok Başarılısınız')
else:
    print('Kaldınız')
print('Not İşlemi Tamamlandı')
