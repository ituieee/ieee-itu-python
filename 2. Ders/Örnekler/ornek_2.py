"""
Bu örnekte dictionary kullanarak bir telefon rehberi oluşturacağız.
Kullanıcı isim ekleyebilir, arayabilir ve tüm rehberi görebilir.
"""

# Boş bir telefon rehberi oluşturalım
phone_book = {}

print("=" * 40)
print("     TELEFON REHBERİ")
print("=" * 40)

# Birkaç kişi ekleyelim
phone_book["Ali Veli"] = "555-1234"
phone_book["Ayşe Yılmaz"] = "555-5678"
phone_book["Mehmet Demir"] = "555-9012"

print("\nRehberde kayıtlı kişiler:")
for isim, numara in phone_book.items():
    print(f"{isim}: {numara}")

# Yeni kişi ekleyelim
print("\n" + "-" * 40)
yeni_isim = input("Eklemek istediğiniz kişinin adı: ")
yeni_numara = input("Telefon numarası: ")
phone_book[yeni_isim] = yeni_numara

print(f"\n{yeni_isim} rehbere eklendi!")

# Arama yapalım
print("\n" + "-" * 40)
aranan = input("Aramak istediğiniz kişinin adı: ")

if aranan in phone_book:
    print(f"{aranan}: {phone_book[aranan]}")
else:
    print("Bu isim rehberde bulunamadı!")

# Toplam kişi sayısı
print(f"\nRehberde toplam {len(phone_book)} kişi kayıtlı.")
