#Not Ortlamasına Göre Harf Atama
gecmenotu=int(input('Geçme Notu Giriniz'))
alinannot=int(input('Aldığınız Notu Giriniz'))
if alinannot>=gecmenotu:
    print('Geçtiniz')
    if alinannot>=90:
        harfnotu='A'
        print('Geçtiniz ve',harfnotu,'ile geçtiniz')
    elif 70>= alinannot <=89:
        harfnotu='B'
        print('Geçtiniz ve',harfnotu,'ile geçtiniz')
    elif 50>= alinannot <=69:
        harfnotu='CB'
        print('Geçtiniz ve',harfnotu,'ile geçtiniz')
    
        
else:
    print('Kaldınız')

print('Not Atama İşlemi Tamamlandı')