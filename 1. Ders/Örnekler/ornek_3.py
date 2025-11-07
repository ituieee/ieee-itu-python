"""
Bu örnekte kullanıcıdan yaş bilgisi alıp, doğum yılını hesaplayan bir program yazacağız.
Ayrıca yaşa göre bazı bilgiler vereceğiz.
"""

# Mevcut yılı tanımlayalım
current_year = 2025

# Kullanıcıdan yaş bilgisi alalım
age = int(input("Yaşınızı girin: "))

# Doğum yılını hesaplayalım
birth_year = current_year - age

# Sonuçları yazdıralım
print(f"\nTahmini doğum yılınız: {birth_year}")
print(f"Bugün itibariyle yaklaşık {age * 365} gün yaşadınız!")
print(f"Bir sonraki doğum gününüzde {age + 1} yaşında olacaksınız.")

# Yaşa göre kategori belirleyelim
if age < 13:
    kategori = "Çocuk"
elif age < 20:
    kategori = "Genç"
elif age < 65:
    kategori = "Yetişkin"
else:
    kategori = "Yaşlı"

print(f"Yaş kategoriniz: {kategori}")
