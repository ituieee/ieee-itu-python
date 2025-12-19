# Operator Overriding Örneği 6: Kitap Sınıfı ve Kütüphane
# Kitapları uzunluğuna göre karşılaştırma ve koleksiyona ekleme işlemleri

class Kitap:
    def __init__(self, başlık, yazar, sayfa_sayısı):
        self.başlık = başlık
        self.yazar = yazar
        self.sayfa_sayısı = sayfa_sayısı
    
    def __lt__(self, diğer):
        """< operatörü: bu kitap daha mı kısa?"""
        return self.sayfa_sayısı < diğer.sayfa_sayısı
    
    def __le__(self, diğer):
        """<= operatörü: bu kitap daha mı kısa veya eşit?"""
        return self.sayfa_sayısı <= diğer.sayfa_sayısı
    
    def __gt__(self, diğer):
        """> operatörü: bu kitap daha mı uzun?"""
        return self.sayfa_sayısı > diğer.sayfa_sayısı
    
    def __ge__(self, diğer):
        """>= operatörü: bu kitap daha mı uzun veya eşit?"""
        return self.sayfa_sayısı >= diğer.sayfa_sayısı
    
    def __eq__(self, diğer):
        """== operatörü: aynı sayı sayfaya mı sahip?"""
        return self.sayfa_sayısı == diğer.sayfa_sayısı
    
    def __ne__(self, diğer):
        """!= operatörü: farklı sayfa sayısına mı sahip?"""
        return self.sayfa_sayısı != diğer.sayfa_sayısı
    
    def __add__(self, diğer):
        """+ operatörü: iki kitabın toplam sayfasını hesapla"""
        if isinstance(diğer, Kitap):
            toplam_sayfa = self.sayfa_sayısı + diğer.sayfa_sayısı
            return f"Toplam {toplam_sayfa} sayfa"
        return None
    
    def __sub__(self, diğer):
        """- operatörü: iki kitab arasındaki sayfa farkı"""
        if isinstance(diğer, Kitap):
            fark = abs(self.sayfa_sayısı - diğer.sayfa_sayısı)
            return f"{fark} sayfa fark"
        return None
    
    def __str__(self):
        return f'"{self.başlık}" - {self.yazar} ({self.sayfa_sayısı} sayfa)'
    
    def __repr__(self):
        return f"Kitap('{self.başlık}', '{self.yazar}', {self.sayfa_sayısı})"


class Kitaplık:
    def __init__(self):
        self.kitaplar = []
    
    def __len__(self):
        """len() fonksiyonu: kütüphanede kaç kitap var?"""
        return len(self.kitaplar)
    
    def __getitem__(self, indeks):
        """[] operatörü: kütüphanedeki n. kitaba erişim"""
        return self.kitaplar[indeks]
    
    def __add__(self, kitap):
        """+ operatörü: kütüphaneyeye yeni kitap ekle"""
        if isinstance(kitap, Kitap):
            self.kitaplar.append(kitap)
            return self
        return self
    
    def __str__(self):
        if not self.kitaplar:
            return "Kitaplık boş"
        
        sonuç = "Kütüphanedeki Kitaplar:\n"
        for i, kitap in enumerate(self.kitaplar, 1):
            sonuç += f"{i}. {kitap}\n"
        return sonuç


# Örnekler
print("=== Kitap Sınıfında Operator Overriding ===\n")

# Kitapları oluşturma
kitap1 = Kitap("Python Programlama", "Guido van Rossum", 450)
kitap2 = Kitap("Veri Yapıları", "Mark Weiss", 320)
kitap3 = Kitap("Yapay Zeka Temelleri", "Stuart Russell", 900)
kitap4 = Kitap("Yazılım Mimarisi", "Robert C. Martin", 320)

print(f"Kitap 1: {kitap1}")
print(f"Kitap 2: {kitap2}")
print(f"Kitap 3: {kitap3}")
print(f"Kitap 4: {kitap4}\n")

# Karşılaştırma operatörleri
print("=== Karşılaştırma Operatörleri ===")
print(f"kitap1 > kitap2: {kitap1 > kitap2} ({kitap1.başlık} daha uzun mu?)")
print(f"kitap2 < kitap3: {kitap2 < kitap3} ({kitap2.başlık} daha kısa mı?)")
print(f"kitap2 == kitap4: {kitap2 == kitap4} (aynı sayfa sayısı mı?)")
print(f"kitap1 != kitap2: {kitap1 != kitap2} (farklı sayfa sayısı mı?)\n")

# Aritmetik operatörleri
print("=== Aritmetik Operatörleri ===")
print(f"kitap1 + kitap2: {kitap1 + kitap2}")
print(f"kitap3 - kitap1: {kitap3 - kitap1}\n")

# Kütüphanede kitapları saklama
print("=== Kütüphanede Kitapları Saklama ===")
kütüphane = Kitaplık()

# Kütüphaneyeye kitapları ekleme
kütüphane = kütüphane + kitap1
kütüphane = kütüphane + kitap2
kütüphane = kütüphane + kitap3
kütüphane = kütüphane + kitap4

print(f"Kütüphanede {len(kütüphane)} kitap vardır\n")
print(kütüphane)

# Kütüphanedeki kitaplara indeks ile erişim
print("=== İndeks ile Erişim ===")
print(f"İlk kitap: {kütüphane[0]}")
print(f"Son kitap: {kütüphane[-1]}\n")

# Kitapları sayfa sayısına göre sıralama
print("=== Kitapları Sayfa Sayısına Göre Sıralama ===")
sıralı = sorted(kütüphane.kitaplar)
for i, kitap in enumerate(sıralı, 1):
    print(f"{i}. {kitap}")
