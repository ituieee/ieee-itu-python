# Ders 1-3: Operatörler ve Bazı Yararlı Fonksiyonlar

## Operatörler

Operatörler, değişkenler ve değerler üzerinde işlemler gerçekleştirmek için kullanılır. Python'da çeşitli operatör türleri vardır:

### Aritmetik Operatörler

Aritmetik operatörler, matematiksel işlemler yapmak için kullanılır. Python'da bulunan aritmetik operatörler şunlardır:

- `+` : Toplama
- `-` : Çıkarma
- `*` : Çarpma
- `/` : Bölme
- `//` : Tam Bölme
- `%` : Modül (Kalan)
- `**` : Üslü

Örnek kullanım:

```python
x = 10
y = 3
print(x + y)  # Çıktı: 13
print(x - y)  # Çıktı: 7
print(x * y)  # Çıktı: 30
print(x / y)  # Çıktı: 3.3333333333333335
print(x // y) # Çıktı: 3
print(x % y)  # Çıktı: 1
print(x ** y) # Çıktı: 1000
```

### Karşılaştırma Operatörleri

Karşılaştırma operatörleri, iki değeri karşılaştırmak için kullanılır ve genellikle boolean (True/False) sonuç döner. Python'da bulunan karşılaştırma operatörleri şunlardır:

- `==` : Eşitlik
- `!=` : Eşitsizlik
- `>`  : Büyüklük
- `<`  : Küçüklük
- `>=` : Büyük veya Eşit
- `<=` : Küçük veya Eşit

Örnek kullanım:

```python
x = 10
y = 5
print(x == y)  # Çıktı: False
print(x != y)  # Çıktı: True
print(x > y)   # Çıktı: True
print(x < y)   # Çıktı: False
print(x >= y)  # Çıktı: True
print(x <= y)  # Çıktı: False
```

### Mantıksal Operatörler

Mantıksal operatörler, boolean değerler üzerinde mantıksal işlemler yapmak için kullanılır. Python'da bulunan mantıksal operatörler şunlardır:

- `and` : Ve
- `or`  : Veya
- `not` : Değil

Örnek kullanım:

```python
x = True
y = False
print(x and y)  # Çıktı: False
print(x or y)   # Çıktı: True
print(not x)    # Çıktı: False
```

### Üyelik Operatörleri
Listeleri ilerleyen derslerde detaylı inceleyeceğiz ancak şimdilik üyelik operatörlerine göz atalım.
Üyelik operatörleri, bir değerin bir koleksiyonda (liste, demet, sözlük vb.) bulunup bulunmadığını kontrol etmek için kullanılır. Python'da bulunan üyelik operatörleri şunlardır:

- `in` : İçinde
- `not in` : İçinde Değil

Örnek kullanım:

```python
liste = [1, 2, 3, 4, 5]
print(3 in liste)      # Çıktı: True
print(6 not in liste)  # Çıktı: True
```

### Kimlik Operatörleri

Kimlik operatörleri, iki nesnenin aynı bellek alanını paylaş olup olmadığını kontrol etmek için kullanılır. Python'da bulunan kimlik operatörleri şunlardır:

- `is` : Aynı
- `is not` : Aynı Değil

Örnek kullanım:

```python
x = [1, 2, 3]
y = x
z = x[:] # Burada z değişkeni x'in bir kopyasıdır.
print(x is y)      # Çıktı: True
print(x is z)      # Çıktı: False
print(x == z)      # Çıktı: True
```

## Bazı Yararlı Fonksiyonlar

Python, çeşitli yerleşik fonksiyonlar sunar. Fonksiyonlara detaylı olarak ilerleyen derslerde değineceğiz, ancak burada bazı temel fonksiyonlara göz atalım:

- `print()`: Ekrana çıktı vermek için kullanılır. (Bu fonksiyonu zaten sıkça kullandık!)
- `input()`: Kullanıcıdan veri girişi almak için kullanılır.

Örnek kullanım:

```python
isim = input("Adınızı girin: ")
print("Merhaba, " + isim + "!")
```
String türündeki verileri kontrol etmek ve dönüştürmek için bazı yararlı fonksiyonlar şunlardır:

- `.upper()`: Stringi büyük harflere dönüştürür.
- `.lower()`: Stringi küçük harflere dönüştürür.
- `.strip()`: Stringin başındaki ve sonundaki boşlukları kaldırır.
- `.format()`: String içerisinde dinamik veri yerleştirmek için kullanılır.
- `.replace()`: Belirtilen bir alt stringi başka bir alt stringle değiştirir.
- `.split()`: Stringi belirli bir ayırıcıya göre parçalara böler ve liste olarak döner.
- `.startswith()`: Stringin belirli bir alt stringle başlayıp başlamadığını kontrol eder.
- `.join()`: Bir listeyi belirli bir ayırıcı kullanarak tek bir stringe dönüştürür.
- `.isalpha()`: Stringin sadece harflerden oluşup oluşmadığını kontrol eder.
- `.isdecimal()`: Stringin sadece rakamlardan oluşup oluşmadığını kontrol eder.

Örnek kullanım:

```python
txt = "merhaba DÜNYA"

print(txt.upper())
print(txt.lower())
print(txt.replace("DÜNYA", "IEEE")) # Evet fonksiyonlar birden fazla parametre alabilir.
print(txt.capitalize())
print(txt.startswith("merh"))
```

Az önce gördüğümüz `format()` fonksiyonu da oldukça kullanışlıdır. Verilerimiz asla sabit kalmadığı için dinamik bir şekilde formatlama yapmamıza olanak tanır. Biraz detaylı inceleyelim:

```python
sayi1 = 6
sayi2 = 5

print("IEEE içerisinde {} komite ve {} ekip bulunur.".format(sayi1, sayi2))
print("IEEE içerisinde {0} komite ve {1} ekip bulunur.".format(sayi1, sayi2))
print("IEEE içerisinde {komite} komite ve {ekip} ekip bulunur.".format(komite = sayi1, ekip = sayi2))
print(f"IEEE içerisinde {sayi1} komite ve {sayi2} ekip bulunur.") 
```
