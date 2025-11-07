"""
Bu örnekte abstraction (soyutlama) kullanarak bir şekil hesaplama sistemi yapacağız.
Abstract base class ile farklı şekiller için ortak arayüz oluşturacağız.
"""

from abc import ABC, abstractmethod
import math

class Sekil(ABC):
    """Abstract base class - tüm şekiller için temel sınıf"""
    
    def __init__(self, isim):
        self.isim = isim
    
    @abstractmethod
    def alan_hesapla(self):
        """Her şekil kendi alan hesaplama yöntemini tanımlamalı"""
        pass
    
    @abstractmethod
    def cevre_hesapla(self):
        """Her şekil kendi çevre hesaplama yöntemini tanımlamalı"""
        pass
    
    def bilgi_goster(self):
        """Şekil bilgilerini gösterir - concrete method"""
        print(f"\n{'=' * 50}")
        print(f"Şekil: {self.isim}")
        print(f"Alan: {self.alan_hesapla():.2f} birim²")
        print(f"Çevre: {self.cevre_hesapla():.2f} birim")
        print(f"{'=' * 50}")


class Kare(Sekil):
    """Kare şekli"""
    
    def __init__(self, kenar):
        super().__init__("Kare")
        self.kenar = kenar
    
    def alan_hesapla(self):
        return self.kenar ** 2
    
    def cevre_hesapla(self):
        return 4 * self.kenar


class Dikdortgen(Sekil):
    """Dikdörtgen şekli"""
    
    def __init__(self, uzunluk, genislik):
        super().__init__("Dikdörtgen")
        self.uzunluk = uzunluk
        self.genislik = genislik
    
    def alan_hesapla(self):
        return self.uzunluk * self.genislik
    
    def cevre_hesapla(self):
        return 2 * (self.uzunluk + self.genislik)


class Daire(Sekil):
    """Daire şekli"""
    
    def __init__(self, yaricap):
        super().__init__("Daire")
        self.yaricap = yaricap
    
    def alan_hesapla(self):
        return math.pi * (self.yaricap ** 2)
    
    def cevre_hesapla(self):
        return 2 * math.pi * self.yaricap


class Ucgen(Sekil):
    """Üçgen şekli (kenar uzunlukları ile)"""
    
    def __init__(self, kenar1, kenar2, kenar3):
        super().__init__("Üçgen")
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.kenar3 = kenar3
    
    def cevre_hesapla(self):
        return self.kenar1 + self.kenar2 + self.kenar3
    
    def alan_hesapla(self):
        # Heron formülü kullanarak alan hesaplama
        s = self.cevre_hesapla() / 2
        alan = math.sqrt(s * (s - self.kenar1) * (s - self.kenar2) * (s - self.kenar3))
        return alan


class Yamuk(Sekil):
    """Yamuk şekli"""
    
    def __init__(self, taban1, taban2, yukseklik, kenar1, kenar2):
        super().__init__("Yamuk")
        self.taban1 = taban1
        self.taban2 = taban2
        self.yukseklik = yukseklik
        self.kenar1 = kenar1
        self.kenar2 = kenar2
    
    def alan_hesapla(self):
        return ((self.taban1 + self.taban2) * self.yukseklik) / 2
    
    def cevre_hesapla(self):
        return self.taban1 + self.taban2 + self.kenar1 + self.kenar2


# Şekilleri oluşturalım ve test edelim
print("=" * 50)
print("GEOMETRİK ŞEKİL HESAPLAMA SİSTEMİ")
print("=" * 50)

# Farklı şekiller oluşturalım
kare = Kare(5)
dikdortgen = Dikdortgen(8, 4)
daire = Daire(3)
ucgen = Ucgen(3, 4, 5)
yamuk = Yamuk(6, 4, 3, 3.5, 3.5)

# Tüm şekilleri bir listede tutalım
sekiller = [kare, dikdortgen, daire, ucgen, yamuk]

# Her şeklin bilgilerini gösterelim
for sekil in sekiller:
    sekil.bilgi_goster()

# Toplam alan hesabı
print("\n" + "=" * 50)
print("TOPLU İSTATİSTİKLER")
print("=" * 50)
toplam_alan = sum(sekil.alan_hesapla() for sekil in sekiller)
toplam_cevre = sum(sekil.cevre_hesapla() for sekil in sekiller)

print(f"Toplam {len(sekiller)} şekil hesaplandı")
print(f"Toplam alan: {toplam_alan:.2f} birim²")
print(f"Toplam çevre: {toplam_cevre:.2f} birim")
print(f"Ortalama alan: {toplam_alan/len(sekiller):.2f} birim²")

# En büyük alana sahip şekil
en_buyuk = max(sekiller, key=lambda s: s.alan_hesapla())
print(f"En büyük alan: {en_buyuk.isim} ({en_buyuk.alan_hesapla():.2f} birim²)")
