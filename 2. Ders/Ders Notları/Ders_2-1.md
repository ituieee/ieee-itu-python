# Ders 2-1: Diziler ve Koşullu İfadeler

## Diziler (Array)


Diziler, Python'da bir değişken de birden fazla veri saklamamızı sağlayan değişken türleridir. Farklı türleri mevcuttur.


__List__

Pythonda en çok kullanılan dizi tipidir. Elemanlar sıralı saklanır, değiştirilebilir ve aynı eleman birden fazla kez bulunabilir.
<br> Bir liste şu şekilde tanımlanır:

```python
liste = [1, 2, 3, 4, 5]
print(liste)  # Çıktı: [1, 2, 3, 4, 5]
```

Elemanlara indeks numaraları ile erişilir. **İndeks numaraları 0'dan başlar.**

```python
print(liste[0])  # Çıktı: 1
print(liste[2])  # Çıktı: 3
print(liste[-1]) # Çıktı: 5 (indeks numarasını negatife çevirdiğimizde sondan başlarız)
```
Aynı yöntemle listemizden alt listeler de oluşturabiliriz:

```python
print(liste[1:4])  # Çıktı: [2, 3, 4] (1. indexten 4. indexe kadar olan elemanlar)
print(liste[:3])   # Çıktı: [1, 2, 3] (başlangıçtan 3. indexe kadar olan elemanlar)
print(liste[2:])   # Çıktı: [3, 4, 5] (2. indexten sona kadar olan elemanlar)
```

__Yararlı fonksiyon ve kavramlar__

- `in` : listede bir elemanın olup olmadığını verir.
- `.count()` parametre olarak girilen elemanın listede kaç tane olduğunu verir.
- `.append()` parametre olarak girilen ifadeyi liste sonuna ekler.
- `.extend()` parametre olarak girilen listeyi listenin sonuna ekler
- `.pop()` parametre olarak girilen index'teki elemanı listeden siler.
- `.remove()` parametre olarak girilen değerdeki elemanları listeden siler.

En çok kullanılan metodları listeledik, diğerlerine [buradan](https://www.w3schools.com/python/python_lists_methods.asp) ulaşabilirsin
<br>Bunların kullanımlarını incelersek:

```python
data = ["İTÜ", "since", 1773, True]

print("İTÜ" in data) # True, çünkü "İTÜ" listede var
print(data.count("1773")) # 0, çünkü string değil integer olarak var 1773

data.append("IEEE") # Liste sonuna "IEEE" ekler
print(data) # Çıktı: ['İTÜ', 'since', 1773, True, 'IEEE']
data.pop(3) # 3. indexteki elemanı siler 
data.remove(1773) # Değeri 1773 olan elemanı siler
print(data.index("IEEE")) # "IEEE" elemanının index numarasını verir
print(data) # Çıktı: ['İTÜ', 'since', 'IEEE']
```
Listede belli bir konumdaki elemanı değiştirmek de mümkündür:

```python
data = [10, 20, 30, 40, 50]
data[2] = 99  # 2. indexteki elemanı 99 ile değiştirir
print(data)  # Çıktı: [10, 20, 99, 40, 50]
```

__Tuple__

Bir diğer dizi türüdür. Elemanlar sıralı depolanır, ancak tuple'lar değiştirilemez. Bu sebeple değişmeyen verilerin saklanmasında oldukça kullanışlıdır. listelerle ortak bir çok metoda ve kullanıma sahiptir.
<br>Tanımlanması ve kullanımı şu şekildedir:

```python
tuple_ornek = (1, 2, 3, 4, 5)
print(tuple_ornek)  # Çıktı: (1, 2, 3, 4, 5)
print(tuple_ornek[0])  # Çıktı: 1
```

Tuple'lar değiştirilemez, bu yüzden eleman ekleme, silme veya değiştirme işlemleri yapılamaz. Ancak, tuple'lar üzerinde indeksleme ve dilimleme işlemleri yapılabilir.

```python
print(tuple_ornek[1:4])  # Çıktı: (2, 3, 4)
tuple_ornek[0] = 10  # Hata! Tuple'lar değiştirilemez
```
__Set__

Setler, benzersiz elemanlardan oluşan sırasız koleksiyonlardır. Yani, bir sette aynı eleman birden fazla kez bulunamaz ve elemanların belirli bir sırası yoktur.<br> Set tanımlaması ve kullanımı şu şekildedir:
```python
set_ornek = {1, 2, 3, 4, 5}
print(set_ornek)  # Çıktı: {1, 2, 3, 4, 5}
```
Setler üzerinde ekleme ve silme işlemleri yapılabilir, ancak indeksleme veya dilimleme işlemleri yapılamaz çünkü setler sırasızdır.

```python
set_ornek.add(6)  # Set'e 6 ekler
print(set_ornek)  # Çıktı: {1, 2, 3, 4, 5, 6}
set_ornek.remove(3)  # Set'ten 3'ü siler
print(set_ornek)  # Çıktı: {1, 2, 4, 5, 6}
```

__Dictionary__

Dictionary'ler, anahtar-değer çiftlerinden oluşan sırasız koleksiyonlardır. Her anahtar benzersizdir ve bir değere karşılık gelir.<br> Dictionary tanımlaması ve kullanımı şu şekildedir:
```python
dict_ornek = {"İsim": "Ali", "Yaş": 19, "Şehir": "İstanbul"}
print(dict_ornek)  # Çıktı: {'İsim': 'Ali', 'Yaş': 19, 'Şehir': 'İstanbul'}
print(dict_ornek["İsim"])  # Çıktı: Ali
```
Dictionary'ler üzerinde ekleme, silme ve güncelleme işlemleri yapılabilir.

```python
dict_ornek["Meslek"] = "Öğrenci"  # Yeni anahtar-değer çifti ekler
print(dict_ornek)  # Çıktı: {'İsim': 'Ali', 'Yaş': 19, 'Şehir': 'İstanbul', 'Meslek': 'Öğrenci'}
del dict_ornek["Yaş"]  # 'Yaş' anahtarını siler
print(dict_ornek)  # Çıktı: {'İsim': 'Ali', 'Şehir': 'İstanbul', 'Meslek': 'Öğrenci'}
dict_ornek["Şehir"] = "Ankara"  # 'Şehir' anahtarının değerini günceller
print(dict_ornek)  # Çıktı: {'İsim': 'Ali', 'Şehir': 'Ankara', 'Meslek': 'Öğrenci'}
``` 

## Koşullu İfadeler

Koşullu ifadeler, belirli bir koşulun doğru olup olmadığını kontrol etmek için kullanılır. Python'da en yaygın kullanılan koşullu ifadeler `if`, `elif` ve `else` anahtar kelimeleri ile oluşturulur.

```python
sayi = "10"
if sayi > 0:
    print("Sayı pozitif.")
elif sayi == 0:
    print("Sayı sıfır.")
else:
    print("Sayı negatif.")
```

Yukarıdaki örnekte ilk defa gördüğümüz bir kavram var: **Girintileme (Indentation)**. Python'da kod blokları girintileme ile belirlenir. `if`, `elif` ve `else` ifadelerinden sonra gelen kod blokları, bu ifadelerin altında ve aynı seviyede girintilenmiş olmalıdır. Genellikle 4 boşluk kullanılır. Modern kod editörleri bu girintilemeyi TAB tuşuna basınca otomatik olarak yapar.

Ayrıca fark ettiğiniz üzere koşullu ifadeyi kullanırken iki nokta üst üste `:` kullanılır. Bu, Python'a bir kod bloğunun başlayacağını belirtir. 

Programlama dillerinde yazım kurallarına "syntax" denir. Python'un syntax'ı diğer dillere göre daha sade ve okunabilir olmasıyla bilinir. Eğer kodunuzu çalıştırdığınızda SyntaxError alıyorsanız, kodunuzun Python'un yazım kurallarına uygun olup olmadığını kontrol etmelisiniz.

if-else yapısında birkaç örnek daha inceleyelim:

```python
sinif = {
    "Ali" : [40, 50, 70],
    "Zehra" : [50, 45, 82],
    "Efe" :  [10, 30, 65]
}

ogrenci = input("Öğrenci adı:")

if(not ogrenci in sinif): # Verilen isim listemizde yoksa
    print("Listede olmayan bir öğrenci adı girdiniz!")

else:
    notlar = sinif[ogrenci]
    toplam = notlar[0] + notlar[1] + notlar[2] # 3 notun toplamak için tüm elemanları ayrı ayrı çekip topladık.
    ortalama = toplam / len(notlar)  # Ortalamayı almak için toplamı listenin eleman sayısı olan 3 e bölüyoruz
    sonuc = round(ortalama, 2) # Küsürattan kurtulalım
    print(sonuc)
```

Bu örnekte, kullanıcıdan bir öğrenci adı alıyoruz ve bu adın `sinif` sözlüğünde olup olmadığını kontrol ediyoruz. Eğer öğrenci adı sözlükte yoksa, kullanıcıya bir uyarı mesajı gösteriyoruz. Eğer öğrenci adı sözlükte varsa, öğrencinin notlarını alıp ortalamasını hesaplıyoruz ve sonucu ekrana yazdırıyoruz.

Mantıksal operatörler de koşullu ifadelerde sıkça kullanılır. Dikkat ettiyseniz if-elif ifadelerinde parantez içinde yazdığımız değerlerin çıktıları `True` veya `False` oluyor. Bunu daha karmaşık koşullar oluşturmak için kullanabiliriz.

```python
a = 0
b = 10

if (a > 10 and b > 10):
    print("a ve b değerleri 10'dan büyük sayılar")

elif (a > 100 or b > 100):
    print("a ve b değerleri 100'den büyük sayılar")

elif (a < 10 and not b > 10):
    print("a değeri 10'dan küçük ve b değeri 10'dan büyük değil")

elif(a != 0 and b == 0):
    print("a değeri 0'a eşit değil ve b değeri 0'a eşit")

else:
    print("diğer koşullar sağlanmadı")
```

**SORU** : Bu döngüde a = 117 and b = 245 koşulu sağlandığında hangi mesaj ekrana yazdırılır? Kodu çalıştırmadan cevabı düşünün ve ardından kodu çalıştırarak cevabınızı kontrol edin.

if-else yapısında iç içe koşullar da oluşturulabilir:

```python
sayi = int(input("Bir sayı girin: "))
if sayi >= 0:
    if sayi == 0:
        print("Sayı sıfır.")
    else:
        print("Sayı pozitif.")
else:
    print("Sayı negatif.")
```

Bu örnekte, ilk `if` ifadesi sayının pozitif, negatif veya sıfır olup olmadığını kontrol eder. Eğer sayı pozitifse, iç içe bir `if` ifadesi kullanılarak sayının sıfır olup olmadığı kontrol edilir.


