"""
Bu örnekte, matematik işlemleri yapan bir modül oluşturacağız.
Farklı fonksiyonlarla faktöriyel, asal sayı kontrolü gibi işlemler yapacağız.
"""

def faktoriyel(n):
    """Bir sayının faktöriyelini hesaplar"""
    if n < 0:
        return "Negatif sayıların faktöriyeli hesaplanamaz!"
    elif n == 0 or n == 1:
        return 1
    else:
        sonuc = 1
        for i in range(2, n + 1):
            sonuc *= i
        return sonuc

def asal_mi(sayi):
    """Bir sayının asal olup olmadığını kontrol eder"""
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def fibonacci(n):
    """İlk n fibonacci sayısını döndürür"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_listesi = [0, 1]
    for i in range(2, n):
        fib_listesi.append(fib_listesi[-1] + fib_listesi[-2])
    return fib_listesi

def mukemmel_kare_mi(sayi):
    """Bir sayının mükemmel kare olup olmadığını kontrol eder"""
    if sayi < 0:
        return False
    karekok = int(sayi ** 0.5)
    return karekok * karekok == sayi

# Test edelim
print("MATEMAT İK İŞLEMLER")
print("=" * 50)

# Faktöriyel testi
print("\n1. Faktöriyel Hesaplama")
sayi = int(input("Bir sayı girin: "))
print(f"{sayi}! = {faktoriyel(sayi)}")

# Asal sayı testi
print("\n2. Asal Sayı Kontrolü")
sayi = int(input("Bir sayı girin: "))
if asal_mi(sayi):
    print(f"{sayi} asal bir sayıdır!")
else:
    print(f"{sayi} asal bir sayı değildir.")

# Fibonacci dizisi
print("\n3. Fibonacci Dizisi")
n = int(input("Kaç fibonacci sayısı görmek istersiniz? "))
print(f"İlk {n} fibonacci sayısı: {fibonacci(n)}")

# Mükemmel kare kontrolü
print("\n4. Mükemmel Kare Kontrolü")
sayi = int(input("Bir sayı girin: "))
if mukemmel_kare_mi(sayi):
    print(f"{sayi} mükemmel bir karedir! (√{sayi} = {int(sayi ** 0.5)})")
else:
    print(f"{sayi} mükemmel bir kare değildir.")
