# Operator Overriding Örneği 5: Kompleks Sayılar (Complex Numbers)
# Kompleks sayılarla toplama, çıkarma ve çarpma işlemlerini gerçekleştirelim

class KompleksSayı:
    def __init__(self, gerçek, sanal):
        self.gerçek = gerçek  # Gerçek kısım
        self.sanal = sanal    # Sanal kısım (i ile çarpılan kısım)
    
    def __add__(self, other):
        """+ operatörü ile iki kompleks sayıyı topla"""
        if isinstance(other, KompleksSayı):
            yeni_gerçek = self.gerçek + other.gerçek
            yeni_sanal = self.sanal + other.sanal
            return KompleksSayı(yeni_gerçek, yeni_sanal)
        return self
    
    def __sub__(self, other):
        """- operatörü ile iki kompleks sayıyı çıkar"""
        if isinstance(other, KompleksSayı):
            yeni_gerçek = self.gerçek - other.gerçek
            yeni_sanal = self.sanal - other.sanal
            return KompleksSayı(yeni_gerçek, yeni_sanal)
        return self
    
    def __mul__(self, other):
        """* operatörü ile iki kompleks sayıyı çarp
        (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        """
        if isinstance(other, KompleksSayı):
            yeni_gerçek = (self.gerçek * other.gerçek) - (self.sanal * other.sanal)
            yeni_sanal = (self.gerçek * other.sanal) + (self.sanal * other.gerçek)
            return KompleksSayı(yeni_gerçek, yeni_sanal)
        elif isinstance(other, (int, float)):
            return KompleksSayı(self.gerçek * other, self.sanal * other)
        return self
    
    def __eq__(self, other):
        """== operatörü ile iki kompleks sayıyı karşılaştır"""
        if isinstance(other, KompleksSayı):
            return self.gerçek == other.gerçek and self.sanal == other.sanal
        return False
    
    def __str__(self):
        """String olarak gösterim"""
        if self.sanal >= 0:
            return f"{self.gerçek} + {self.sanal}i"
        else:
            return f"{self.gerçek} - {abs(self.sanal)}i"
    
    def __repr__(self):
        return f"KompleksSayı({self.gerçek}, {self.sanal})"


# Örnekler
print("=== Kompleks Sayılarla Operator Overriding ===\n")

# Sayılar oluşturma
z1 = KompleksSayı(3, 4)      # 3 + 4i
z2 = KompleksSayı(1, 2)      # 1 + 2i
z3 = KompleksSayı(3, 4)      # 3 + 4i

print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"z3 = {z3}\n")

# Toplama
print("Toplama (z1 + z2):")
sonuç_toplama = z1 + z2
print(f"{z1} + {z2} = {sonuç_toplama}\n")

# Çıkarma
print("Çıkarma (z1 - z2):")
sonuç_çıkarma = z1 - z2
print(f"{z1} - {z2} = {sonuç_çıkarma}\n")

# Çarpma
print("Çarpma (z1 * z2):")
sonuç_çarpma = z1 * z2
print(f"{z1} * {z2} = {sonuç_çarpma}")
print(f"Kontrol: (3+4i)(1+2i) = (3*1-4*2) + (3*2+4*1)i = -5 + 10i\n")

# Skalar ile çarpma
print("Skalar ile çarpma (z1 * 2):")
sonuç_skalar = z1 * 2
print(f"{z1} * 2 = {sonuç_skalar}\n")

# Eşitlik kontrolü
print("Eşitlik kontrolü:")
print(f"z1 == z3: {z1 == z3}")
print(f"z1 == z2: {z1 == z2}")
