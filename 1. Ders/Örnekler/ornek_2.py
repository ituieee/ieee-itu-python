"""
Bu örneğimizde, bir öğrencinin notlarını alan ve ortalamasını hesaplayan bir program hazırlayacağız. 
"""

# Öğrencinin notlarını alalım
vize1 = int(input("1. Vize Notu: ")) # Burası bir yorum satırıdır
vize2 = int(input("2. Vize Notu: "))
final = int(input("Final Notu: "))

# Ortalama hesaplayalım
ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)

# Ortalamayı bir üst tam sayıya yuvarlayalım
ortalama = round(ortalama)

# Ortalamayı yazdıralım
print(f"Ortalama: {ortalama}")

# Ortalama 50'den küçükse kaldı, 50'den büyükse geçti, geçme durumunu true/false olarak yazdıralım

gecme_durumu = ortalama >= 50

print(f"Geçme Durumu: {gecme_durumu}")
