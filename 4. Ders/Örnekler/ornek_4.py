"""
Bu örnekte bir kütüphane yönetim sistemi yapacağız.
Kalıtım, soyutlama ve çok biçimlilik (polymorphism) kavramlarını kullanacağız.
"""

from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Materyal(ABC):
    """Abstract base class - tüm kütüphane materyalleri için"""
    
    materyal_sayisi = 0
    
    def __init__(self, baslik, yazar):
        self.baslik = baslik
        self.yazar = yazar
        self.odunc_durumu = False
        self.odunc_alan = None
        self.odunc_tarihi = None
        Materyal.materyal_sayisi += 1
        self.id = Materyal.materyal_sayisi
    
    @abstractmethod
    def odunc_suresi(self):
        """Her materyal türü kendi ödünç süresini belirler"""
        pass
    
    def odunc_ver(self, kisi_adi):
        """Materyali ödünç verir"""
        if not self.odunc_durumu:
            self.odunc_durumu = True
            self.odunc_alan = kisi_adi
            self.odunc_tarihi = datetime.now()
            iade_tarihi = self.odunc_tarihi + timedelta(days=self.odunc_suresi())
            print(f"✓ '{self.baslik}' {kisi_adi} tarafından ödünç alındı")
            print(f"  İade tarihi: {iade_tarihi.strftime('%d/%m/%Y')}")
        else:
            print(f"✗ '{self.baslik}' şu anda {self.odunc_alan} tarafından kullanılıyor")
    
    def iade_et(self):
        """Materyali iade eder"""
        if self.odunc_durumu:
            gun_gecti = (datetime.now() - self.odunc_tarihi).days
            ceza = max(0, (gun_gecti - self.odunc_suresi()) * 2)  # Geç iade için günlük 2 TL
            
            print(f"✓ '{self.baslik}' iade edildi")
            if ceza > 0:
                print(f"  ⚠️  Geç iade cezası: {ceza} TL")
            
            self.odunc_durumu = False
            self.odunc_alan = None
            self.odunc_tarihi = None
        else:
            print(f"✗ '{self.baslik}' zaten kütüphanede")
    
    def bilgi_goster(self):
        """Materyal bilgilerini gösterir"""
        durum = f"Ödünçte ({self.odunc_alan})" if self.odunc_durumu else "Mevcut"
        print(f"[{self.id}] {self.baslik} - {self.yazar} | {durum}")


class Kitap(Materyal):
    """Kitap sınıfı"""
    
    def __init__(self, baslik, yazar, sayfa_sayisi):
        super().__init__(baslik, yazar)
        self.sayfa_sayisi = sayfa_sayisi
    
    def odunc_suresi(self):
        return 14  # Kitaplar 14 gün ödünç verilebilir


class Dergi(Materyal):
    """Dergi sınıfı"""
    
    def __init__(self, baslik, yazar, sayi):
        super().__init__(baslik, yazar)
        self.sayi = sayi
    
    def odunc_suresi(self):
        return 7  # Dergiler 7 gün ödünç verilebilir


class DVD(Materyal):
    """DVD sınıfı"""
    
    def __init__(self, baslik, yonetmen, sure):
        super().__init__(baslik, yonetmen)
        self.sure = sure
    
    def odunc_suresi(self):
        return 3  # DVD'ler 3 gün ödünç verilebilir


class Kutuphane:
    """Kütüphane yönetim sınıfı"""
    
    def __init__(self, isim):
        self.isim = isim
        self.materyaller = []
    
    def materyal_ekle(self, materyal):
        """Kütüphaneye yeni materyal ekler"""
        self.materyaller.append(materyal)
        print(f"✓ '{materyal.baslik}' kütüphaneye eklendi")
    
    def materyal_listele(self, sadece_mevcut=False):
        """Tüm materyalleri listeler"""
        print(f"\n{'=' * 70}")
        print(f"{self.isim} - Materyal Listesi")
        print(f"{'=' * 70}")
        
        for materyal in self.materyaller:
            if sadece_mevcut and materyal.odunc_durumu:
                continue
            materyal.bilgi_goster()
        
        print(f"{'=' * 70}")
    
    def materyal_ara(self, arama_kelime):
        """Başlıkta arama yapar"""
        bulunanlar = [m for m in self.materyaller if arama_kelime.lower() in m.baslik.lower()]
        
        if bulunanlar:
            print(f"\n'{arama_kelime}' araması için {len(bulunanlar)} sonuç bulundu:")
            for m in bulunanlar:
                m.bilgi_goster()
        else:
            print(f"'{arama_kelime}' için sonuç bulunamadı")
    
    def istatistikler(self):
        """Kütüphane istatistiklerini gösterir"""
        toplam = len(self.materyaller)
        odunç = sum(1 for m in self.materyaller if m.odunc_durumu)
        mevcut = toplam - odunç
        
        print(f"\n📊 Kütüphane İstatistikleri")
        print(f"Toplam materyal: {toplam}")
        print(f"Ödünçte: {odunç}")
        print(f"Mevcut: {mevcut}")


# Kütüphane sistemini test edelim
print("=" * 70)
print("KÜTÜPHANE YÖNETİM SİSTEMİ")
print("=" * 70)

# Kütüphane oluştur
kutuphane = Kutuphane("İTÜ Kütüphanesi")

# Materyaller ekle
kitap1 = Kitap("Python Programlama", "Ahmet Yılmaz", 350)
kitap2 = Kitap("Veri Bilimi", "Ayşe Demir", 420)
dergi1 = Dergi("Bilim ve Teknik", "TÜBİTAK", 550)
dvd1 = DVD("Python Eğitim Seti", "Mehmet Kaya", 180)

kutuphane.materyal_ekle(kitap1)
kutuphane.materyal_ekle(kitap2)
kutuphane.materyal_ekle(dergi1)
kutuphane.materyal_ekle(dvd1)

# Materyalleri listele
kutuphane.materyal_listele()

# Ödünç verme işlemleri
print("\n" + "-" * 70)
kitap1.odunc_ver("Ali Yılmaz")
dergi1.odunc_ver("Zeynep Kaya")

# Mevcut materyalleri listele
kutuphane.materyal_listele(sadece_mevcut=True)

# İade işlemi
print("\n" + "-" * 70)
kitap1.iade_et()

# Arama yap
print("\n" + "-" * 70)
kutuphane.materyal_ara("Python")

# İstatistikler
print("\n" + "-" * 70)
kutuphane.istatistikler()
