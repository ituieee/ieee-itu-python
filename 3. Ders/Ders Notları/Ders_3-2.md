# Ders 3-2 : Dekoratörler ve Lambda Fonksiyonları

## Dekoratörler
Dekoratörler, bir fonksiyonu alıp ona yeni işlevsellik ekleyen özel fonksiyonlardır. Dekoratörler, genellikle fonksiyonların davranışını değiştirmek veya genişletmek için kullanılır. Dekoratörler, `@` sembolü ile uygulanır.
Örnek bir dekoratör tanımlayalım:

```python
def example_decorator(func):
    def wrapper():
        print("Fonksiyon çalışmadan öncesi.")
        func()
        print("Fonksiyon çalıştıktan sonrası.")        
    return wrapper

@example_decorator
def example_function():
    print("Hello World!")
```

Çıktısı şöyle olacaktır:
```
Fonksiyon çalışmadan öncesi.
Hello World!
Fonksiyon çalıştıktan sonrası.
```

Başka bir örnek olarak, bir fonksiyonun çalışma süresini ölçen bir dekoratör yapalım:

```python
import time

def zamanlayici(fonksiyon):
    def sarmalayıcı(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} fonksiyonu {bitis - baslangic} saniye sürdü.")
        return sonuc
    return sarmalayıcı

@zamanlayici
def uzun_sureli_islem():
    time.sleep(2)
    print("İşlem tamamlandı.")

uzun_sureli_islem()
```

Burada, `zamanlayici` dekoratörü, `uzun_sureli_islem` fonksiyonunun çalışma süresini ölçer ve sonucu ekrana yazdırır.

## Lambda Fonksiyonları
Lambda fonksiyonları, tek satırlık anonim fonksiyonlardır. `lambda` anahtar kelimesi ile tanımlanırlar ve genellikle kısa ve basit işlemler için kullanılırlar. Lambda fonksiyonları, normal fonksiyonlara göre daha kısa ve özdür. Örnek bir lambda fonksiyonu tanımlayalım:

```python
topla = lambda x, y: x + y
print(topla(3, 5))  # Çıktı: 8
```
Lambda fonksiyonları, genellikle `map()`, `filter()` ve `reduce()` gibi fonksiyonlarla birlikte kullanılırlar. Örneğin, bir liste içindeki sayıları iki katına çıkarmak için `map()` fonksiyonu ile birlikte bir lambda fonksiyonu kullanabiliriz:

```python
sayilar = [1, 2, 3, 4, 5]
iki_kat = list(map(lambda x: x * 2, sayilar))
print(iki_kat)  # Çıktı: [2, 4, 6, 8, 10]
```
Benzer şekilde, `filter()` fonksiyonu ile bir liste içindeki çift sayıları seçmek için bir lambda fonksiyonu kullanabiliriz:

```python
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
print(cift_sayilar)  # Çıktı: [2, 4]
```

