import random
import os

# Zar adedini belirlemek için kullanıcıdan giriş alır.
def zar_adedi():
    while True:
        try:
            zar_sayisi = input('Zar adedi: ')
            gecerli_cevaplar = ['1', 'bir', 'iki', '2']
            if zar_sayisi not in gecerli_cevaplar:
                raise ValueError('Sadece 1 veya 2 girebilirsiniz')
            elif zar_sayisi == 'q':
                Exit_Game()
            else:
                return zar_sayisi
        except ValueError as hata :
            print(hata)

# Zarları atmak için gerekli işlemleri gerçekleştirir.
def zar_at():
    min_deger = 1
    max_deger = 6
    tekrar_at = 'e'

    # Kullanıcı tekrar atmaya devam etmek istediği sürece döngüyü sürdürür.
    while tekrar_at.lower() == 'evet' or tekrar_at.lower() == 'e':
        # Ekranı temizler (platforma bağlı olarak 'clear' veya 'cls' komutunu kullanır).
        os.system('clear')  # macOS için 'clear' komutu
        miktar = zar_adedi()

        # 1 veya 2 zar atma durumlarına göre işlemleri gerçekleştirir.
        if miktar == '2' or miktar == 'iki':
            
            print('Zarlar atılıyor...')
            zar_1 = random.randint(min_deger, max_deger)
            zar_2 = random.randint(min_deger, max_deger)

            # Zar değerlerini ve toplamı ekrana yazdırır.
            print('Değerler şunlar:')
            print('Zar Bir: ', zar_1)
            print('Zar İki: ', zar_2)
            print('Toplam: ', zar_1 + zar_2)

            # Kullanıcıya tekrar atmaya devam edip etmeyeceğini sorar.
            tekrar_at = input('Tekrar Atmak İster Misiniz?  ')
            
        else:
            print('Zar atılıyor...')
            zar_1 = random.randint(min_deger, max_deger)

            # Tek bir zar atıldığında değeri ekrana yazdırır.
            print(f'Değer: {zar_1}')

            # Kullanıcıya tekrar atmaya devam edip etmeyeceğini sorar.
            tekrar_at = input('Tekrar Atmak İster Misiniz?')
            
            
def Exit_Game():
    print('Oyundan Çıkılıyor,İyi GÜnler :)')
    exit()
            

if __name__ == '__main__':
    # Programın ana bölümü, zar_at() fonksiyonunu çağırarak oyunu başlatır.
    zar_at()
