# Ders 2-2: Döngüler ve Error Handling

## Döngüler

Döngüler, belirli bir koşul sağlandığı sürece bir kod bloğunu tekrar tekrar çalıştırmak için kullanılır. Python'da en yaygın kullanılan döngü türleri `for` döngüsü ve `while` döngüsüdür.

### For Döngüsü

`for` döngüsü, bir dizinin (liste, tuple, set, vb.) elemanları üzerinde döngü yapmak için kullanılır. Örnek:

```python
meyveler = ["elma", "armut", "muz"]
for meyve in meyveler:
    print(meyve)
```

Yukarıdaki örnekte, `meyveler` listesindeki her bir meyve için döngü çalışır ve meyve adı ekrana yazdırılır.

### While Döngüsü

`while` döngüsü, belirli bir koşul doğru olduğu sürece döngüyü çalıştırır. Örnek:

```python
sayi = 0
while sayi < 5:
    print(sayi)
    sayi += 1
```

Bu örnekte, `sayi` değişkeni 5'ten küçük olduğu sürece döngü çalışır ve her seferinde `sayi` 1 artırılır.

### For ve While Döngülerinin Karşılaştırılması
- `for` döngüsü, genellikle belirli bir koleksiyonun elemanları üzerinde işlem yapmak için kullanılır.
- `while` döngüsü ise, belirli bir koşul sağlandığı sürece çalışır ve genellikle koşula bağlı işlemler için tercih edilir.

Daha iyi oturması için bir metafor kullanabiliriz:

- 50 Tane şınav çekmak istiyorsanız ve her şınavı tek tek sayacaksanız, `for` döngüsü kullanırsınız.
- Ancak, şınav çekmeye devam edeceksiniz ama ne zaman duracağınızı bilmiyorsanız, örneğin "Artık yoruldum" dediğinizde duracaksanız, o zaman `while` döngüsü kullanırsınız.

### Break ve Continue

Döngülerde `break` ve `continue` anahtar kelimeleri de kullanılır.

- `break`: Döngüyü sonlandırmak için kullanılır.
- `continue`: Döngünün o anki iterasyonunu atlayıp bir sonraki iterasyona geçmek için kullanılır.

Örnek:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

Yukarıdaki örnekte, `i` 5 olduğunda döngü sonlanır ve 0'dan 4'e kadar olan sayılar ekrana yazdırılır.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

Bu örnekte ise, `i` çift sayı olduğunda o iterasyon atlanır ve sadece tek sayılar ekrana yazdırılır.

## Error Handling

Hataları yönetmek için Python'da `try` ve `except` blokları kullanılır. Bu bloklar, hata oluşabilecek kodları güvenli bir şekilde çalıştırmak için kullanılır.

Örnek:

```python
try:
    sayi = int(input("Bir sayı girin: "))
    print("Girdiğiniz sayı:", sayi)
except ValueError:
    print("Geçersiz bir sayı girdiniz.")
```

Yukarıdaki örnekte, kullanıcıdan bir sayı girmesi istenir. Eğer kullanıcı geçersiz bir giriş yaparsa (örneğin bir harf girerse), `ValueError` hatası yakalanır ve kullanıcıya bir hata mesajı gösterilir.

```python
try:
    sonuc = 10 / 0
except ZeroDivisionError:
    print("Bir sayıyı sıfıra bölemezsiniz.")
```

Bu örnekte ise, sıfıra bölme hatası yakalanır ve kullanıcıya uygun bir mesaj gösterilir.

```python
try:
    dosya = open("varolmayan_dosya.txt", "r")
except FileNotFoundError:
    print("Dosya bulunamadı.")
```

Bu örnekte, var olmayan bir dosya açılmaya çalışıldığında `FileNotFoundError` hatası yakalanır ve kullanıcıya bir hata mesajı gösterilir.

Bunların yanında `else` ve `finally` blokları da kullanılabilir:
- `else`: Hata oluşmadığında çalıştırılacak kod bloğunu belirtir.
- `finally`: Hata oluşsa da oluşmasa da her durumda çalıştırılacak kod bloğunu belirtir.

```python
try:
    sayi = int(input("Bir sayı girin: "))
except ValueError:
    print("Geçersiz bir sayı girdiniz.")
else:
    print("Girdiğiniz sayı:", sayi)
finally:
    print("Program sona erdi.")
```

Error handling yaparken sıkça kullanılan bir yapı da `raise` ifadesidir. Bu ifade, bilerek bir hata oluşturmak için kullanılır.

```python
pozitif_sayi = int(input("Pozitif bir sayı girin: "))
if pozitif_sayi < 0:
    raise ValueError("Negatif bir sayı girdiniz!")
else:
    print("Girdiğiniz pozitif sayı:", pozitif_sayi)
``` 

Bu örnekte, kullanıcıdan pozitif bir sayı girmesi istenir. Eğer kullanıcı negatif bir sayı girerse, `ValueError` hatası bilerek oluşturulur ve kullanıcıya bir hata mesajı gösterilir. Eğer pozitif bir sayı girilirse, sayı ekrana yazdırılır.

Hatalar hakkında daha detaylı bilgi edinmek için Python'un resmi dokümantasyonuna bakabilirsiniz: https://docs.python.org/3/tutorial/errors.html


    