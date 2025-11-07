"""
Bu örnekte while döngüsü kullanarak bir tahmin oyunu yapacağız.
Bilgisayar bir sayı tutar, kullanıcı tahmin eder.
"""

import random

print("=" * 40)
print("   SAYI TAHMİN OYUNU")
print("=" * 40)

# Bilgisayar 1-100 arasında rastgele bir sayı tutsun
tutulan_sayi = random.randint(1, 100)

# Tahmin sayısını tutacak değişken
tahmin_sayisi = 0
max_tahmin = 7  # Kullanıcıya 7 tahmin hakkı verelim

print(f"\n1 ile 100 arasında bir sayı tuttum.")
print(f"Toplam {max_tahmin} tahmin hakkınız var.\n")

# Oyun döngüsü
while tahmin_sayisi < max_tahmin:
    kalan_hak = max_tahmin - tahmin_sayisi
    print(f"Kalan hak: {kalan_hak}")
    
    # Kullanıcıdan tahmin alalım
    try:
        tahmin = int(input("Tahmininiz: "))
    except:
        print("Lütfen geçerli bir sayı girin!\n")
        continue
    
    tahmin_sayisi += 1
    
    # Tahmini kontrol edelim
    if tahmin == tutulan_sayi:
        print(f"\n🎉 Tebrikler! {tahmin_sayisi}. tahminde doğru sayıyı buldunuz!")
        print(f"Doğru cevap: {tutulan_sayi}")
        break
    elif tahmin < tutulan_sayi:
        print("⬆️  Daha büyük bir sayı deneyin!\n")
    else:
        print("⬇️  Daha küçük bir sayı deneyin!\n")
else:
    # While döngüsü normal biterse (break ile çıkılmazsa)
    print(f"\n😞 Tahmin hakkınız bitti!")
    print(f"Doğru cevap: {tutulan_sayi}")
