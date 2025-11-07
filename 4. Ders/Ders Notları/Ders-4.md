# Ders 4: Nesne Tabanlı Programlama (OOP)

## Sınıflar (Classes)

Python, nesne tabanlı bir programlama dilidir (Object Oriented Programming - OOP). Bu demek oluyor ki, Python'da kullandığımız neredeyse tüm yapılar birer nesnedir: string, int, list, dict, fonksiyon gibi pek çok şey.

Sınıflar (class), objeler yaratırken kullandığımız birer taslak gibidir. Geçtiğimiz haftalarda `type()` fonksiyonunu kullandığımızda aldığımız çıktıya tekrar göz atalım:

```python
a = 5
b = "IEEE"
c = []
def d():
    pass

print(type(a))  # Çıktı: <class 'int'>
print(type(b))  # Çıktı: <class 'str'>
print(type(c))  # Çıktı: <class 'list'>
print(type(d))  # Çıktı: <class 'function'>
```

Göreceğiniz üzere, `a` değişkeni aslında `int` sınıfına ait bir örnek. Burada **class (sınıf)** ve **object (nesne)** kavramları önemlidir:

- **Class (Sınıf)**: Bir taslaktır, blueprint'tir
- **Object (Nesne)**: O class kullanılarak üretilmiş her bir örnektir (instance)

Integer, function, string, list birer class; yukarıda yarattığımız a, b, c, d ise birer nesnedir.

### Sınıf Tanımlamak

Bir sınıf tanımlamak için `class` anahtar kelimesi kullanılır:

```python
class MyClass:
    x = 5
```

Bu şekilde `MyClass` adında bir sınıf oluşturduk. Bu sınıftan oluşturacağımız objelerin taslağı bu olacak.

### Obje Oluşturmak

Bu sınıftan obje oluşturmak için:

```python
nesne1 = MyClass()
nesne2 = MyClass()
print(nesne1.x)  # Çıktı: 5
print(type(nesne2))  # Çıktı: <class '__main__.MyClass'>
```

`nesne1` ve `nesne2`, artık `MyClass` sınıfına ait objeler. `x` ise bu objelere ait bir özellik (attribute). Bir objeye ait özelliklere ve methodlara erişmek için `obje.özellik` formatını kullanırız.

### Constructor (__init__ Methodu)

Gerçek hayatta, birbirine tıpatıp benzeyen objeler değil, aynı taslaktan çıkan farklı objelere ihtiyaç duyarız. Bunun için `__init__` methodunu kullanırız:

```python
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil
    
    def yazdir(self):
        return f"{self.yil} model {self.marka} {self.model}"

benim_arac = Araba("BMW", "M2", "2022")
print(benim_arac.yazdir())  # Çıktı: 2022 model BMW M2
print(benim_arac.yil)       # Çıktı: 2022
```

### self Parametresi

Yukarıdaki örnekte yeni bir şey fark ettiniz: `self` parametresi. `self`, o sınıfa ait o an erişilen objeyi temsil eder. Bu parametre, Python tarafından otomatik olarak verilir. Sınıfın içerisinde method tanımlarken ilk parametre olarak yazarız, ancak sınıfın dışında bu methodu çağırırken `self` için bir değer yollamayız.

### Dunder Methods (Magic Methods)

Python tarafından tanımlanan özel methodlara "Dunder Methods" veya "Magic Methods" denir. İsimlerinin başında ve sonunda `__` işareti bulunur. En yaygın kullanılanlar:

- `__init__(self, ..)`: Obje ilk yaratılırken çağrılır. Constructor olarak bilinir.
- `__str__(self)`: `print()` veya `str()` fonksiyonu ile obje string'e çevrilmek istendiğinde çağrılır.
- `__len__(self)`: `len()` fonksiyonu ile objenin uzunluğu sorulduğunda çağrılır.

Daha fazla Dunder Method'a [buradan](https://nitesh-yadav.medium.com/dunder-methods-in-python-really-crazy-functions-3455ecb6472d) ulaşabilirsiniz.

### Class ve Instance Attribute'ları

```python
class Calisan:
    sirket = "İTÜ"  # Bu bir class attribute: Bu sınıfa ait her obje için aynı
    
    def __init__(self, ad, soyad, maas):
        self.ad = ad        # Bunlar instance attribute: Her obje için farklı olabilir
        self.soyad = soyad
        self.maas = maas
    
    def __str__(self):
        return f"{self.ad} {self.soyad}"
    
    def zam(self, miktar):
        self.maas += miktar

# İki farklı obje tanımlanması
calisan1 = Calisan("Mike", "Tyson", 1000)
calisan2 = Calisan("Mustafa", "Yurtseven", 1200)

# Attribute'ların kullanımı
print(calisan1)           # Çıktı: Mike Tyson
print(calisan1.maas)      # Çıktı: 1000
print(calisan1.sirket)    # Çıktı: İTÜ
print(calisan2.maas)      # Çıktı: 1200

# Method çağırma
calisan2.zam(100)
print(calisan2.maas)      # Çıktı: 1300

# Direkt olarak bir objenin attribute'unun değiştirilmesi
calisan1.ad = "John"
print(calisan1)           # Çıktı: John Tyson

# Var olmayan yeni attribute eklemek
calisan1.saat = 40
```

**Önemli Not**: Class attribute'lar tüm objeler tarafından paylaşılır. Instance attribute'lar ise her objeye özgüdür.

## Kalıtım (Inheritance)

Kalıtım, bir sınıftan diğerine özelliklerin ve methodların aktarılmasını sağlar. Özellikleri veren sınıfa **Parent Class (Üst Sınıf)**, özellikleri alan sınıfa **Child Class (Alt Sınıf)** adı verilir.

### Temel Kalıtım

```python
class Insan:  # Parent class
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
        self.is_durumu = "çalışan"
    
    def dogum_gunu(self):
        self.yas += 1

class Ogrenci(Insan):  # Child class
    def __init__(self, ad, yas, not_ortalamasi):
        super().__init__(ad, yas)  # Parent class'ın __init__'ini çağırır
        self.not_ortalamasi = not_ortalamasi
        self.is_durumu = "öğrenci"
    
    def not_ver(self, yeni_not):
        self.not_ortalamasi = yeni_not

# Kullanım
ali = Insan("Ali", 21)
hasan = Ogrenci("Hasan", 21, 3.0)

print(ali.yas)           # Çıktı: 21
print(hasan.not_ortalamasi)  # Çıktı: 3.0
ali.dogum_gunu()
print(hasan.yas)           # Çıktı: 22
print(hasan.is_durumu)     # Çıktı: öğrenci
```

### super() Fonksiyonu

`super()` fonksiyonu, parent class'a erişmemizi sağlar. Child class'ta parent class'ın methodlarını çağırmak istediğimizde kullanırız. Yukarıdaki örnekte, `Ogrenci` class'ının `__init__` methodunda `super().__init__(ad, yas)` yazarak `Insan` class'ının `__init__` methodunu çağırdık.

### Override (Üzerine Yazma)

Child class'ta parent class'ın bir methodunu yeniden tanımlarsak, parent'taki method override edilir (üzerine yazılır). Child class'ta tanımlanan method, parent'taki methodun yerini alır.

```python
class Hayvan:
    def ses_cikar(self):
        print("Hayvan ses çıkarıyor")

class Kedi(Hayvan):
    def ses_cikar(self):
        print("Miyav!")

class Kopek(Hayvan):
    def ses_cikar(self):
        print("Hav hav!")

kedi = Kedi()
kopek = Kopek()

kedi.ses_cikar()   # Çıktı: Miyav!
kopek.ses_cikar()  # Çıktı: Hav hav!
```

### Çoklu Kalıtım Hiyerarşisi

Kalıtım yapısını dallandırarak daha karmaşık hiyerarşiler oluşturabiliriz:

```python
class Canlilar:
    def __init__(self):
        self.canli = True

class Omurgalilar(Canlilar):
    def __init__(self):
        super().__init__()
        self.omurga = True

class Memeliler(Omurgalilar):
    def __init__(self):
        super().__init__()
        self.sut_salgisi = True

class Insan(Memeliler):
    def __init__(self, ad):
        super().__init__()
        self.ad = ad
        self.akilli = True

ali = Insan("Ali")
print(ali.canli)      # Çıktı: True
print(ali.omurga)     # Çıktı: True
print(ali.sut_salgisi)  # Çıktı: True
print(ali.akilli)     # Çıktı: True
```

Bu yapıda `Insan` sınıfına ait bir obje, override etmediği sürece, tüm üst sınıfların özellik ve methodlarını içerir.

Bu şekilde teorik anlatımla tam olarak kafanıza oturması ve alışmanız pek mümkün değil. Bu sebeple bu haftaki derste sayı olarak fazla örneğe bakacağız. [Class](https://www.w3schools.com/python/python_classes.asp) ve [Inheritance](https://www.w3schools.com/python/python_inheritance.asp) yapıları için bu bağlantılara tıklayarak çok daha çeşitli örnekler görebilirsiniz.

## Soyutlama (Abstraction)

Soyutlama (abstraction), nesne tabanlı programlamanın temel prensiplerinden biridir. Karmaşık detayları gizleyerek, kullanıcıya sadece gerekli bilgileri gösterme prensibidir. Gerçek hayattan bir örnek vermek gerekirse: Bir arabayı kullanırken motor nasıl çalışıyor bilmemize gerek yoktur. Sadece gaza basıp, frene basıp, direksiyonu kullanarak arabayı kullanabiliriz. İşte bu soyutlamadır.

Python'da soyutlama için **Abstract Base Classes (ABC)** kullanılır. Abstract class'lar, doğrudan instance oluşturulamayan, ancak diğer class'ların miras alabileceği şablon class'lardır.

### Abstract Class Tanımlama

Abstract class tanımlamak için `abc` modülünü kullanırız:

```python
from abc import ABC, abstractmethod

class Sekil(ABC):  # Abstract base class
    @abstractmethod
    def alan_hesapla(self):
        pass
    
    @abstractmethod
    def cevre_hesapla(self):
        pass
```

Yukarıdaki örnekte `Sekil` bir abstract class'tır. `@abstractmethod` dekoratörü ile işaretlenen methodlar, bu class'tan türetilen tüm child class'larda **mutlaka** tanımlanmalıdır.

### Abstract Class'tan Türetme

Abstract class'tan türeyen bir child class, tüm abstract methodları implement etmelidir:

```python
from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan_hesapla(self):
        pass
    
    @abstractmethod
    def cevre_hesapla(self):
        pass

class Dikdortgen(Sekil):
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    
    def alan_hesapla(self):
        return self.uzunluk * self.genislik
    
    def cevre_hesapla(self):
        return 2 * (self.uzunluk + self.genislik)

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
    
    def alan_hesapla(self):
        return 3.14 * self.yaricap ** 2
    
    def cevre_hesapla(self):
        return 2 * 3.14 * self.yaricap

# Kullanım
dikdortgen = Dikdortgen(5, 3)
print(dikdortgen.alan_hesapla())    # Çıktı: 15
print(dikdortgen.cevre_hesapla())   # Çıktı: 16

daire = Daire(7)
print(daire.alan_hesapla())         # Çıktı: 153.86
print(daire.cevre_hesapla())        # Çıktı: 43.96
```

**Önemli**: Abstract class'tan doğrudan obje oluşturamazsınız:

```python
# sekil = Sekil()  # Hata! Abstract class'tan instance oluşturulamaz
```

### Neden Soyutlama Kullanırız?

1. **Kod Organizasyonu**: Benzer özelliklere sahip class'lar için ortak bir arayüz tanımlarız.
2. **Zorunlu Implementasyon**: Child class'ların belirli methodları implement etmesini garanti ederiz.
3. **Esneklik**: Farklı implementasyonlar oluşturabiliriz ama ortak bir yapı korunur.
4. **Güvenlik**: Karmaşık detaylar gizlenir, sadece gerekli arayüz gösterilir.

### Daha Gelişmiş Bir Örnek

```python
from abc import ABC, abstractmethod

class Odeme(ABC):
    @abstractmethod
    def odeme_yap(self, miktar):
        pass
    
    @abstractmethod
    def odeme_iptal(self):
        pass

class KrediKartiOdeme(Odeme):
    def __init__(self, kart_no):
        self.kart_no = kart_no
    
    def odeme_yap(self, miktar):
        print(f"Kredi kartı ile {miktar} TL ödeme yapıldı.")
        print(f"Kart No: {self.kart_no}")
    
    def odeme_iptal(self):
        print("Kredi kartı ödemesi iptal edildi.")

class HavaleOdeme(Odeme):
    def __init__(self, iban):
        self.iban = iban
    
    def odeme_yap(self, miktar):
        print(f"Havale ile {miktar} TL ödeme yapıldı.")
        print(f"IBAN: {self.iban}")
    
    def odeme_iptal(self):
        print("Havale ödemesi iptal edildi.")

# Kullanım
kart_odeme = KrediKartiOdeme("1234-5678-9012-3456")
kart_odeme.odeme_yap(150)
# Çıktı:
# Kredi kartı ile 150 TL ödeme yapıldı.
# Kart No: 1234-5678-9012-3456

havale_odeme = HavaleOdeme("TR123456789")
havale_odeme.odeme_yap(200)
# Çıktı:
# Havale ile 200 TL ödeme yapıldı.
# IBAN: TR123456789
```

### Abstract ve Concrete Methods Birlikte

Bir abstract class, hem abstract hem de normal (concrete) methodlar içerebilir:

```python
from abc import ABC, abstractmethod

class Calisan(ABC):
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
    
    # Normal method - tüm child class'lar kullanabilir
    def tam_ad(self):
        return f"{self.ad} {self.soyad}"
    
    # Abstract method - child class'lar implement etmeli
    @abstractmethod
    def maas_hesapla(self):
        pass

class TamZamanli(Calisan):
    def __init__(self, ad, soyad, aylik_maas):
        super().__init__(ad, soyad)
        self.aylik_maas = aylik_maas
    
    def maas_hesapla(self):
        return self.aylik_maas

class Freelance(Calisan):
    def __init__(self, ad, soyad, saatlik_ucret, calisma_saati):
        super().__init__(ad, soyad)
        self.saatlik_ucret = saatlik_ucret
        self.calisma_saati = calisma_saati
    
    def maas_hesapla(self):
        return self.saatlik_ucret * self.calisma_saati

# Kullanım
tam_zamanli = TamZamanli("Ali", "Veli", 15000)
print(tam_zamanli.tam_ad())      # Çıktı: Ali Veli
print(tam_zamanli.maas_hesapla()) # Çıktı: 15000

freelance = Freelance("Ayşe", "Yılmaz", 100, 120)
print(freelance.tam_ad())         # Çıktı: Ayşe Yılmaz
print(freelance.maas_hesapla())   # Çıktı: 12000
```

### Soyutlama ile İlgili Önemli Notlar

1. Abstract class'tan doğrudan instance (obje) oluşturamazsınız.
2. Abstract methodları implement etmeyen child class da abstract olarak kalır ve ondan da instance oluşturamazsınız.
3. `@abstractmethod` dekoratörü, methodun abstract olduğunu belirtir.
4. Abstract class'lar, bir arayüz (interface) sağlar ve polymorphism'i destekler.
5. Python'da interface yoktur, ancak abstract class'lar benzer bir amaç için kullanılır.

## Özet

Bu derste nesne tabanlı programlamanın temel kavramlarını öğrendik:

1. **Sınıflar ve Objeler**: Class'lar taslaktır, objeler bu taslaktan üretilen örneklerdir.
2. **Constructor (`__init__`)**: Obje yaratılırken çağrılan özel method.
3. **self Parametresi**: Objenin kendisini temsil eder.
4. **Attribute'lar**: Class attribute (tüm objeler için ortak) ve instance attribute (her objeye özel).
5. **Kalıtım**: Bir class'ın başka bir class'tan özellik ve methodları miras alması.
6. **super()**: Parent class'a erişimi sağlar.
7. **Override**: Child class'ta parent class'ın methodlarını yeniden tanımlama.
8. **Soyutlama**: Karmaşık detayları gizleyerek ortak arayüzler oluşturma.

Bu kavramları iyi anlamak için bol bol pratik yapmanız önerilir. Farklı senaryolar için kendi class'larınızı oluşturun ve kalıtım yapılarını deneyin!
