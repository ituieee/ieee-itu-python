# Ders 1-2: Temel Kavramlar

## Değişkenler ve Veri Tipleri

Python'da değişkenler, verileri saklamak için kullanılır. Değişkenler herhangi bir veri tipini içerebilir, örneğin sayılar, metinler (string), listeler, vb.

### Değişken Tanımlama

Python'da bir değişken tanımlamak için, değişkenin adını yazıp eşittir (`=`) işareti ile bir değer atamanız yeterlidir. Örneğin:

```python
sayi = 10
metin = "Merhaba"
durum = True # Neden böyle bir değer atadık?
```

Tanımlanan değişkenler daha sonra programın herhangi bir yerinde kullanılabilir. Tanımladığımız değişkenlerin değerlerini ekrana yazdırmak için `print()` fonksiyonunu kullanabilirsiniz:

```python
print(sayi)   # Çıktı: 10
print(metin)  # Çıktı: Merhaba
print(durum)  # Çıktı: True
```
Bir değişkenin değerini değiştirmek de oldukça basittir. Yeni bir değer atayarak mevcut değeri güncelleyebilirsiniz:

```python
sayi = 20
print(sayi)  # Çıktı: 20
sayi = sayi + 5
print(sayi)  # Çıktı: 25
sayi = 2
print(sayi)  # Çıktı: 2
```

Python'da değişken adları harfler, rakamlar ve alt çizgi (`_`) içerebilir, ancak rakamla başlayamaz. Ayrıca, Python anahtar kelimeleri (örneğin `if`, `for`, `while` gibi) değişken adı olarak kullanılamaz.

### Veri tipleri

Python veriyi saklamak için çeşitli veri tipleri sunar. Sayıları saklamak için kullandığımız veri tiplerine bakacak olursak:
- `int`: Tam sayılar için kullanılır. Örneğin: `5`, `-3`, `0`
- `float`: Ondalıklı sayılar için kullanılır. Örneğin: `3.14`, `-0.001`, `2.0`
- `complex`: Karmaşık sayılar için kullanılır. Örneğin: `2 + 3j`, `-1 + 0j`

Bu veri tiplerini kullanarak değişkenler tanımlayabiliriz:

```python
a = 10          # int
b = 3.14        # float
c = 2 + 3j      # complex
print(type(a))  # Çıktı: <class 'int'>
print(type(b))  # Çıktı: <class 'float'>
print(type(c))  # Çıktı: <class 'complex'>
```
Bu sayı tipleri birbirine dönüştürülebilir. Örneğin, bir `int` değeri `float`'a dönüştürmek için `float()` fonksiyonunu kullanabilirsiniz:

```python
x = 5          # int
y = float(x)   # float
print(x)       # Çıktı: 5
print(type(x)) # Çıktı: <class 'int'>
print(y)       # Çıktı: 5.0
print(type(y)) # Çıktı: <class 'float'>
```
Metin (string) veri tipi, karakter dizilerini saklamak için kullanılır. Metinler tek tırnak (`'`) veya çift tırnak (`"`) içinde tanımlanabilir:

```python
metin1 = 'Merhaba'
metin2 = "Dünya"
print(metin1)  # Çıktı: Merhaba
print(metin2)  # Çıktı: Dünya
print(type(metin1)) # Çıktı: <class 'str'>
```
Stringler de aynı şekilde başka türlere dönüştürülebilir. Örneğin, bir sayıyı string'e dönüştürmek için `str()` fonksiyonunu kullanabilirsiniz:

```python
sayi = 100
metin = str(sayi)
print(sayi)       # Çıktı: 100
print(type(sayi)) # Çıktı: <class 'int'>
print(metin)      # Çıktı: 100
print(type(metin))# Çıktı: <class 'str'>
```
Boolean (bool) veri tipi, sadece iki değerden birini alabilir: `True` (doğru) veya `False` (yanlış). Genellikle koşullu ifadelerde kullanılır:

```python
durum1 = True
durum2 = False
print(durum1)  # Çıktı: True
print(durum2)  # Çıktı: False
print(type(durum1)) # Çıktı: <class 'bool'>
```


