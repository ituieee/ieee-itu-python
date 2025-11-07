"""
Bu örnekte, kullanıcıdan alınan metni analiz eden fonksiyonlar yazacağız.
Sesli harf sayısı, kelime sayısı gibi istatistikleri hesaplayacağız.
"""

def sesli_harf_say(metin):
    """Metindeki sesli harf sayısını döndürür"""
    sesli_harfler = "aeıioöuüAEIİOÖUÜ"
    sayac = 0
    for harf in metin:
        if harf in sesli_harfler:
            sayac += 1
    return sayac

def kelime_say(metin):
    """Metindeki kelime sayısını döndürür"""
    kelimeler = metin.split()
    return len(kelimeler)

def karakter_say(metin):
    """Metindeki karakter sayısını döndürür (boşluksuz)"""
    return len(metin.replace(" ", ""))

def en_uzun_kelime(metin):
    """Metindeki en uzun kelimeyi döndürür"""
    kelimeler = metin.split()
    if kelimeler:
        return max(kelimeler, key=len)
    return ""

def metin_analizi(metin):
    """Tüm analizleri birleştiren ana fonksiyon"""
    print("\n" + "=" * 50)
    print("METİN ANALİZİ")
    print("=" * 50)
    print(f"Metin: {metin}")
    print("-" * 50)
    print(f"Toplam karakter sayısı (boşluksuz): {karakter_say(metin)}")
    print(f"Toplam kelime sayısı: {kelime_say(metin)}")
    print(f"Sesli harf sayısı: {sesli_harf_say(metin)}")
    print(f"En uzun kelime: {en_uzun_kelime(metin)} ({len(en_uzun_kelime(metin))} harf)")
    print("=" * 50)

# Programı çalıştıralım
print("Metin Analiz Programı")
kullanici_metni = input("Analiz edilecek metni girin: ")
metin_analizi(kullanici_metni)
