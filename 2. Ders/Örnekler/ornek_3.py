"""
Bu örnekte liste üzerinde çeşitli işlemler yapacağız.
Kullanıcıdan alınan sayıları listeye ekleyip, istatistiklerini hesaplayacağız.
"""

# Boş bir liste oluşturalım
sayilar = []

print("Sayı Listesi Programı")
print("(Durdurmak için 'q' yazın)\n")

# Kullanıcıdan sayılar alalım
while True:
    girdi = input("Bir sayı girin: ")
    
    if girdi.lower() == 'q':
        break
    
    try:
        sayi = float(girdi)
        sayilar.append(sayi)
        print(f"✓ {sayi} listeye eklendi")
    except:
        print("✗ Lütfen geçerli bir sayı girin!")

# Liste boş değilse istatistikleri gösterelim
if len(sayilar) > 0:
    print("\n" + "=" * 40)
    print("İSTATİSTİKLER")
    print("=" * 40)
    
    # Listeyi yazdıralım
    print(f"Girilen sayılar: {sayilar}")
    
    # Eleman sayısı
    print(f"Toplam eleman sayısı: {len(sayilar)}")
    
    # En büyük ve en küçük
    print(f"En büyük sayı: {max(sayilar)}")
    print(f"En küçük sayı: {min(sayilar)}")
    
    # Toplam ve ortalama
    toplam = sum(sayilar)
    ortalama = toplam / len(sayilar)
    print(f"Toplam: {toplam}")
    print(f"Ortalama: {ortalama:.2f}")
    
    # Sıralı hali
    sayilar.sort()
    print(f"Küçükten büyüğe sıralı: {sayilar}")
    
    # Pozitif ve negatif sayılar
    pozitif = [s for s in sayilar if s > 0]
    negatif = [s for s in sayilar if s < 0]
    print(f"Pozitif sayılar: {len(pozitif)} adet")
    print(f"Negatif sayılar: {len(negatif)} adet")
else:
    print("\nListeye hiç sayı eklenmedi!")
