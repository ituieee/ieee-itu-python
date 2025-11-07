"""
Bu örnekte bir banka hesabı sistemi oluşturacağız.
Sınıflar kullanarak hesap oluşturma, para yatırma, çekme işlemleri yapacağız.
"""

class BankaHesabi:
    """Temel banka hesabı sınıfı"""
    
    hesap_sayisi = 0  # Class attribute - toplam hesap sayısı
    
    def __init__(self, hesap_sahibi, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye
        BankaHesabi.hesap_sayisi += 1
        self.hesap_no = f"TR{1000 + BankaHesabi.hesap_sayisi}"
    
    def para_yatir(self, miktar):
        """Hesaba para yatırır"""
        if miktar > 0:
            self.bakiye += miktar
            print(f"✓ {miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("✗ Geçersiz miktar!")
    
    def para_cek(self, miktar):
        """Hesaptan para çeker"""
        if miktar > 0:
            if miktar <= self.bakiye:
                self.bakiye -= miktar
                print(f"✓ {miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")
            else:
                print("✗ Yetersiz bakiye!")
        else:
            print("✗ Geçersiz miktar!")
    
    def bakiye_goster(self):
        """Hesap bakiyesini gösterir"""
        print(f"💰 Bakiye: {self.bakiye} TL")
    
    def __str__(self):
        return f"Hesap No: {self.hesap_no} | Hesap Sahibi: {self.hesap_sahibi} | Bakiye: {self.bakiye} TL"


class VadesizHesap(BankaHesabi):
    """Vadesiz hesap - ek özelliklerle"""
    
    def __init__(self, hesap_sahibi, bakiye=0):
        super().__init__(hesap_sahibi, bakiye)
        self.islem_ucreti = 2  # Her işlemde 2 TL ücret
    
    def para_cek(self, miktar):
        """Para çekme işleminde ücret kesilir"""
        toplam = miktar + self.islem_ucreti
        if toplam <= self.bakiye:
            self.bakiye -= toplam
            print(f"✓ {miktar} TL çekildi ({self.islem_ucreti} TL işlem ücreti)")
            print(f"Kalan bakiye: {self.bakiye} TL")
        else:
            print("✗ Yetersiz bakiye! (İşlem ücreti dahil)")


class VadeliHesap(BankaHesabi):
    """Vadeli hesap - faiz kazandırır"""
    
    def __init__(self, hesap_sahibi, bakiye=0, faiz_orani=0.05):
        super().__init__(hesap_sahibi, bakiye)
        self.faiz_orani = faiz_orani  # Yıllık %5 faiz
    
    def faiz_ekle(self):
        """Hesaba faiz ekler"""
        faiz = self.bakiye * self.faiz_orani
        self.bakiye += faiz
        print(f"✓ {faiz:.2f} TL faiz eklendi. Yeni bakiye: {self.bakiye:.2f} TL")
    
    def para_cek(self, miktar):
        """Vadeli hesaptan para çekmek için ceza var"""
        print("⚠️  Vadeli hesaptan erken çekimde %10 ceza uygulanır.")
        ceza = miktar * 0.1
        toplam = miktar + ceza
        if toplam <= self.bakiye:
            self.bakiye -= toplam
            print(f"✓ {miktar} TL çekildi ({ceza:.2f} TL ceza)")
            print(f"Kalan bakiye: {self.bakiye:.2f} TL")
        else:
            print("✗ Yetersiz bakiye!")


# Programı test edelim
print("=" * 60)
print("BANKA HESAP SİSTEMİ")
print("=" * 60)

# Farklı hesap türleri oluşturalım
hesap1 = BankaHesabi("Ahmet Yılmaz", 1000)
hesap2 = VadesizHesap("Ayşe Demir", 500)
hesap3 = VadeliHesap("Mehmet Kaya", 2000, 0.08)

print(f"\n{hesap1}")
print(f"{hesap2}")
print(f"{hesap3}")

# İşlemler yapalım
print("\n" + "-" * 60)
print("HESAP 1 İŞLEMLERİ (Normal Hesap)")
print("-" * 60)
hesap1.para_yatir(500)
hesap1.para_cek(200)
hesap1.bakiye_goster()

print("\n" + "-" * 60)
print("HESAP 2 İŞLEMLERİ (Vadesiz Hesap)")
print("-" * 60)
hesap2.para_yatir(300)
hesap2.para_cek(100)  # İşlem ücreti kesilecek
hesap2.bakiye_goster()

print("\n" + "-" * 60)
print("HESAP 3 İŞLEMLERİ (Vadeli Hesap)")
print("-" * 60)
hesap3.faiz_ekle()
hesap3.para_cek(500)  # Ceza uygulanacak
hesap3.bakiye_goster()

print(f"\n Toplam açılan hesap sayısı: {BankaHesabi.hesap_sayisi}")
