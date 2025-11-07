"""
Bu örnekte, liste ve dictionary kullanarak bir to-do list (yapılacaklar listesi) uygulaması yapacağız.
Modüler fonksiyonlar kullanarak program yazacağız.
"""

def gorev_ekle(gorevler, gorev):
    """Yeni bir görev ekler"""
    gorevler.append({"gorev": gorev, "tamamlandi": False})
    print(f"✓ '{gorev}' görevi eklendi!")

def gorevleri_listele(gorevler):
    """Tüm görevleri listeler"""
    if not gorevler:
        print("Henüz görev eklenmemiş!")
        return
    
    print("\n" + "=" * 60)
    print("YAPILACAKLAR LİSTESİ")
    print("=" * 60)
    for index, gorev in enumerate(gorevler, 1):
        durum = "✓" if gorev["tamamlandi"] else "○"
        print(f"{index}. [{durum}] {gorev['gorev']}")
    print("=" * 60)

def gorev_tamamla(gorevler, index):
    """Bir görevi tamamlanmış olarak işaretler"""
    if 0 <= index < len(gorevler):
        gorevler[index]["tamamlandi"] = True
        print(f"✓ '{gorevler[index]['gorev']}' tamamlandı!")
    else:
        print("Geçersiz görev numarası!")

def gorev_sil(gorevler, index):
    """Bir görevi siler"""
    if 0 <= index < len(gorevler):
        silinen = gorevler.pop(index)
        print(f"✓ '{silinen['gorev']}' silindi!")
    else:
        print("Geçersiz görev numarası!")

def istatistikler(gorevler):
    """Görev istatistiklerini gösterir"""
    toplam = len(gorevler)
    tamamlanan = sum(1 for g in gorevler if g["tamamlandi"])
    kalan = toplam - tamamlanan
    
    print(f"\n📊 Toplam görev: {toplam}")
    print(f"✓ Tamamlanan: {tamamlanan}")
    print(f"○ Kalan: {kalan}")
    if toplam > 0:
        print(f"📈 Tamamlanma oranı: %{(tamamlanan/toplam)*100:.1f}")

# Ana program
gorevler = []

print("=" * 60)
print("YAPILACAKLAR LİSTESİ UYGULAMASI")
print("=" * 60)

while True:
    print("\n1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görevi Tamamla")
    print("4. Görev Sil")
    print("5. İstatistikler")
    print("6. Çıkış")
    
    secim = input("\nSeçiminiz (1-6): ")
    
    if secim == "1":
        gorev = input("Görev: ")
        gorev_ekle(gorevler, gorev)
    
    elif secim == "2":
        gorevleri_listele(gorevler)
    
    elif secim == "3":
        gorevleri_listele(gorevler)
        try:
            index = int(input("Tamamlanacak görev numarası: ")) - 1
            gorev_tamamla(gorevler, index)
        except:
            print("Geçersiz giriş!")
    
    elif secim == "4":
        gorevleri_listele(gorevler)
        try:
            index = int(input("Silinecek görev numarası: ")) - 1
            gorev_sil(gorevler, index)
        except:
            print("Geçersiz giriş!")
    
    elif secim == "5":
        istatistikler(gorevler)
    
    elif secim == "6":
        print("Programdan çıkılıyor. Hoşça kalın!")
        break
    
    else:
        print("Geçersiz seçim! Lütfen 1-6 arası bir sayı girin.")
