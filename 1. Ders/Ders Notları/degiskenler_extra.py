# Adım 1: var isminde bir değişken oluşturuyoruz ve ona 42 sayısını atıyoruz
# Python'da aynı ismi farklı şeyler için kullanabiliriz (ama tavsiye edilmez!)
var = 42
print(f"Adım 1: var:{var} (Değişken tipi: {type(var)})")

# Adım 2: Şimdi var ismine bir string atıyoruz (bu adım string(var) metoduyla aynı değildir!)
# Değişken tamamen değişti ve artık bir string tutuyor
var = "Merhaba, Dünya!"
print(f"Adım 2: var:{var} (Değişken tipi: {type(var)})")

# Adım 3: Şimdi var ismini bir fonksiyon için kullanıyoruz
# Bu fonksiyon aldığı sayının karesini hesaplıyor (x ** 2 = x'in karesi)
def var(x):
    return x ** 2

print(f"Adım 3: var(5): {var(5)} (Değişken tipi: {type(var)})")

# Adım 4: Şimdi var ismini bir sınıf (class) için kullanıyoruz
# Bu sınıf bir değer tutuyor ve çarpma işlemi yapabiliyor
class var:
    def __init__(self, value):
        self.value = value

    def multiply(self, factor):
        return self.value * factor
    
# Sonrasında bu var sınıfından çarpma işlemini çağırıyoruz (İlerleyen konularda detaylı anlatılacak)
print(f"Adım 4: {var(10).multiply(3)} (Değişken tipi: {type(var)})")

# SONUÇ:
# Birden fazla değişkene aynı ismi vermek mümkündür ancak bu, önceki değerin üzerine yazılmasına neden olur. 
# Bu nedenle, değişken isimlendirmesinde dikkatli olunmalı ve farklı isimler tercih edilmelidir.
